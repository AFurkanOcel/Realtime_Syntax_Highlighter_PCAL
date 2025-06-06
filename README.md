# Gerçek Zamanlı Sözdizimi Vurgulayıcı (PCAL için)

Bu proje, **gerçek zamanlı ve biçimsel dilbilgisine dayalı** bir sözdizimi vurgulayıcıdır.  
Kullanıcı yazdıkça, yazdığı metin anında analiz edilerek en az 5 farklı token türü renklendirilir.  
Proje tamamen sıfırdan geliştirilmiştir ve **herhangi bir sözdizimi vurgulama kütüphanesi kullanılmamıştır**.

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

| Token Türü    | Açıklama                      |
|----------------|-------------------------------|
| Tanımlayıcılar | Değişken ve fonksiyon isimleri |
| Sayılar        | Tam sayılar                    |
| Operatörler    | `+`, `-`, `*`, `/` vb.         |
| Atamalar       | `=` işareti                    |
| Noktalama      | `,`, `(`, `)`, `?` gibi simgeler |

---

## 📺 Tanıtım Videosu

Aşağıdaki bağlantıdan uygulamanın tanıtım videosuna ulaşabilirsiniz:

🔗 [Google Drive Video Bağlantısı](https://www.youtube.com/watch?v=eCkWtttOFr0)

---

## 📄 Makale

Projede kullanılan yöntemleri ve geliştirme sürecini anlatan detaylı yazı:

🔗 [Makale Bağlantısı](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/makale.pdf)

---

## 📘 Dokümantasyon Özeti

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

🔗 [Proje Raporu (PDF)](https://github.com/AFurkanOcel/Realtime_Syntax_Highlighter_PCAL/blob/main/rapor.pdf)

---

## 👤 Geliştirici

**Ahmet Furkan Öcel**  
Bilgisayar Mühendisliği Öğrencisi  
Bursa Teknik Üniversitesi

---
