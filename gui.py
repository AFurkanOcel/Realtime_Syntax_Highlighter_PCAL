import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from PIL import Image, ImageTk
from lexer import lexer
from parser import parse, ParseError

# Token renk atamaları
def get_colors(is_dark_mode):
    if is_dark_mode:
        return {
            "IDENTIFIER": "sky blue",
            "NUMBER": "green",
            "OPERATOR": "orange",
            "EQUALS": "orange",
            "QUESTION": "purple",
            "DELIMITER": "purple",
            "PAREN": "magenta",
        }
    else:
        return {
            "IDENTIFIER": "blue",
            "NUMBER": "green",
            "OPERATOR": "orange",
            "EQUALS": "orange",
            "QUESTION": "purple",
            "DELIMITER": "purple",
            "PAREN": "magenta",
        }

class PCAL_GUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.minsize(400, 300)
        self.root.title("PCAL Editor")

        icon = PhotoImage(file="settings.ico")
        root.iconphoto(True, icon)

        self.is_dark_mode = False
        self.colors = get_colors(self.is_dark_mode)

        # Grid yapılandırması
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=0)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(2, weight=0)

        # Satır numaraları
        self.line_numbers = tk.Text(
            root,
            width=4,
            padx=4,
            takefocus=0,
            border=0,
            background="lightgrey",
            state="disabled",
            font=("Consolas", 14),
        )
        self.line_numbers.grid(row=0, column=0, sticky="ns")

        self.text = tk.Text(root, wrap="word", font=("Consolas", 14), undo=True)
        self.text.grid(row=0, column=1, sticky="nsew")

        self.scrollbar = tk.Scrollbar(root, command=self.on_scroll)
        self.scrollbar.grid(row=0, column=2, sticky="ns")
        self.text.config(yscrollcommand=self.on_textscroll)

        self.output = tk.Text(root, height=5, bg="#f0f0f0", font=("Consolas", 12))
        self.output.grid(row=1, column=0, columnspan=3, sticky="ew", padx=5, pady=(5, 0))

        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=5)

        tk.Button(self.button_frame, text="Run", command=self.run_code).pack(
            side="left", padx=5
        )
        tk.Button(self.button_frame, text="Clear", command=self.clear_all).pack(
            side="left", padx=5
        )
        tk.Button(self.button_frame, text="Open File", command=self.open_file).pack(
            side="left", padx=5
        )

        self.size_label = tk.Label(self.button_frame, text="")
        self.size_label.pack(side="left", padx=15)

        self.load_theme_images()
        self.theme_button = tk.Button(
            self.button_frame, image=self.theme_button_image, command=self.toggle_theme
        )
        self.theme_button.pack(side="right", padx=10)

        self.root.bind("<Configure>", lambda event: self.update_size_label())

        self.text.bind("<MouseWheel>", self.sync_scroll)
        self.text.bind("<Button-4>", self.sync_scroll)  # Linux için yukarı kaydırma
        self.text.bind("<Button-5>", self.sync_scroll)  # Linux için aşağı kaydırma

        # Kod yazıldıkça otomatik renklendirme
        self.text.bind("<KeyRelease>", lambda event: self.highlight_tokens())

        self.update_size_label()
        self.apply_theme_colors()  # Başlangıç teması için renkleri uygula

    def load_theme_images(self):
        dark_img = Image.open("dark.png").resize((20, 20), Image.LANCZOS)
        light_img = Image.open("light.png").resize((20, 20), Image.LANCZOS)
        self.dark_photo = ImageTk.PhotoImage(dark_img)
        self.light_photo = ImageTk.PhotoImage(light_img)
        # Başlangıçta light mod simgesi
        self.theme_button_image = self.dark_photo

    def update_size_label(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.size_label.config(text=f"Size: {w} x {h}")
        self.update_line_numbers()

    def update_line_numbers(self):
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", tk.END)

        first_visible = self.text.index("@0,0")
        last_visible = self.text.index(f"@0,{self.text.winfo_height()}")

        start_line = int(first_visible.split(".")[0])
        end_line = int(last_visible.split(".")[0])

        line_numbers_string = "\n".join(str(i) for i in range(start_line, end_line + 1))
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state="disabled")

    def on_scroll(self, *args):
        self.text.yview(*args)
        self.line_numbers.yview(*args)
        self.update_line_numbers()

    def on_textscroll(self, *args):
        self.scrollbar.set(*args)
        self.line_numbers.yview_moveto(args[0])
        self.update_line_numbers()

    def sync_scroll(self, event):
        if event.num == 4 or event.delta > 0:
            self.text.yview_scroll(-1, "units")
            self.line_numbers.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.text.yview_scroll(1, "units")
            self.line_numbers.yview_scroll(1, "units")
        return "break"

    def highlight_tokens(self):
        code = self.text.get("1.0", tk.END)
        if not code.strip():
            # Kod boşsa tüm tagleri temizle
            for tag in self.colors:
                self.text.tag_remove(tag, "1.0", tk.END)
            return

        tokens = lexer(code)

        # Önce eski tag'leri temizle
        for tag in self.colors:
            self.text.tag_remove(tag, "1.0", tk.END)

        for token in tokens:
            start = index_to_position(code, token["start"])
            end = index_to_position(code, token["end"])
            self.text.tag_add(token["type"], start, end)

        self.apply_theme_colors()

    def apply_theme_colors(self):
        for token_type, color in self.colors.items():
            self.text.tag_config(token_type, foreground=color)

    def run_code(self):
        self.highlight_tokens()
        code = self.text.get("1.0", tk.END)
        tokens = lexer(code)
        try:
            results = parse(tokens)
            self.output.delete("1.0", tk.END)
            for line in results:
                self.output.insert(tk.END, line + "\n")
        except ParseError as e:
            self.output.delete("1.0", tk.END)
            self.output.insert(tk.END, "Error: " + str(e))

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("PCAL Files", "*.pcal")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)
            self.highlight_tokens()
            self.update_line_numbers()

    def clear_all(self):
        self.text.delete("1.0", tk.END)
        self.output.delete("1.0", tk.END)
        self.update_line_numbers()

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        self.colors = get_colors(self.is_dark_mode)

        if self.is_dark_mode:
            self.text.config(bg="#1e1e1e", fg="white", insertbackground="white")
            self.line_numbers.config(bg="#2d2d2d", fg="white")
            self.output.config(bg="#1e1e1e", fg="white")
            self.theme_button.config(image=self.light_photo)
        else:
            self.text.config(bg="white", fg="black", insertbackground="black")
            self.line_numbers.config(bg="lightgrey", fg="black")
            self.output.config(bg="#f0f0f0", fg="black")
            self.theme_button.config(image=self.dark_photo)

        self.apply_theme_colors()
        self.update_line_numbers()


def index_to_position(code, index):

    line = code.count("\n", 0, index) + 1
    if line == 1:
        col = index
    else:
        last_nl = code.rfind("\n", 0, index)
        col = index - last_nl - 1
    return f"{line}.{col}"


if __name__ == "__main__":
    root = tk.Tk()
    app = PCAL_GUI(root)
    root.mainloop()