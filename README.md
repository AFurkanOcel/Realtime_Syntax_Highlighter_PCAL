# Gerçek Zamanlı Sözdizimi Vurgulayıcı (PCAL için)

Bu proje, **gerçek zamanlı ve biçimsel dilbilgisine dayalı** bir sözdizimi vurgulayıcıdır.  
Kullanıcı yazdıkça, yazdığı metin anında analiz edilerek en az 5 farklı token türü renklendirilir.  
Proje tamamen sıfırdan geliştirilmiştir ve **herhangi bir sözdizimi vurgulama kütüphanesi kullanılmamıştır**.

<img width="498" height="412" alt="pcal" src="https://github.com/user-attachments/assets/0dea591d-a954-4379-841e-b5c705cf0be8" />    
<img width="498" height="412" alt="pcal_dark" src="https://github.com/user-attachments/assets/060a749a-c3fc-4a8f-9759-5b9c61deab8a" />

## 🔍 Proje Özeti

Uygulama aşağıdaki temel bileşenlerden oluşur:

- **Lexical Analyzer (Lexer)**: Giriş metnini düzenli ifadelere göre tokenize eder.
- **Syntax Analyzer (Parser)**: Token dizisini bağlamdan bağımsız gramerle kontrol eder.
- **Vurgulama Motoru**: Token tiplerine göre renk ataması yapar.
- **Arayüz (GUI)**: Tkinter ile geliştirilmiş olup kullanıcı yazarken anında vurgulama sağlar.

> ⚠️ Herhangi bir hazır vurgulama kütüphanesi kullanılmamıştır.

## 🛠 Kullanılan Teknolojiler

- **Programlama Dili**: Python 3
- **Arayüz**: Tkinter
- **Parser Türü**: Top-Down (Yukarıdan Aşağıya) - Recursive Descent
- **Lexer Yöntemi**: Durum Diyagramı & Programatik Uygulama
- **Dil**: PCAL (basit yapılı, eğitim amaçlı sahte bir programlama dili)

---

## ✅ Vurgulanan Token Türleri

| Token Türü   | Açıklama                                                                 |
|--------------|--------------------------------------------------------------------------|
| IDENTIFIER   | Değişken veya fonksiyon isimlerini temsil eder. Harflerden oluşur.      |
| NUMBER       | Tam sayılardan oluşan sabit sayısal değerlerdir.                        |
| OPERATOR     | Toplama, çıkarma, çarpma, bölme gibi temel matematiksel operatörlerdir. |
| EQUALS       | Atama yapmak için kullanılan eşittir (`=`) sembolüdür.                  |
| QUESTION     | İşlemin sonucunu almak için kullanılan soru işaretidir (`?`).           |
| DELIMITER    | Satır sonunu belirtmek için kullanılan ayraçtır (bu projede `,`).       |
| PAREN        | İşlem önceliği belirtmek için kullanılan parantezlerdir. (`(` ve `)`)   |

---

## 📺 Tanıtım Videosu

Aşağıdaki bağlantıdan uygulamanın tanıtım videosuna ulaşabilirsiniz:

🔗 [Google Drive Video Bağlantısı](https://www.youtube.com/watch?v=eCkWtttOFr0)

---

## 📄 Makale

Projede kullanılan yöntemleri ve geliştirme sürecini anlatan detaylı yazı:

🔗 [Makale Bağlantısı](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/makale.pdf)

---

## 📘 Dokümantasyon

🔗 [Proje Raporu (PDF)](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/rapor.pdf) – Detaylı teknik dokümantasyon ve geliştirme sürecine ilişkin tüm açıklamaları bu raporda görüntüleyebilirsiniz.

### ➤ Dil ve Gramer Seçimi
Proje, PCAL adlı sade yapılı, öğretici bir dille gerçekleştirildi. Kendi grameri tanımlandı ve uygulandı.

### ➤ Sözdizimi Analizi
Recursive Descent yöntemiyle yukarıdan aşağıya sözdizimi analizi yapıldı. Giriş, tanımlı dilbilgisine göre doğrulandı.

### ➤ Lexical Analiz
Lexer, Python ve düzenli ifadelerle sıfırdan geliştirildi. Durum diyagramına dayalı olarak çalışır.

### ➤ Parser Yöntemi
Yukarıdan aşağıya (top-down) yaklaşımıyla, recursive descent tekniğiyle analiz yapılır.

### ➤ Vurgulama Şeması
Her token türü için farklı renkler atanarak `Text` bileşeninde `tag_config()` ile uygulanır.

### ➤ Arayüz Uygulaması
Kullanıcı yazarken anında analiz ve renklendirme yapılır. Arayüz, sade ve kullanıcı dostudur.

---

## 👤 Geliştirici

**Ahmet Furkan Öcel**  
