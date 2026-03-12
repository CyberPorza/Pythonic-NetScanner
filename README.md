🛡️ Pythonic Network Scanner & Recon Tool
Bu proje, ağ üzerindeki aktif cihazların açık kapılarını (portlarını) ve bu portlarda çalışan servisleri hızlıca tespit etmek için geliştirilmiş, hafif ve etkili bir keşif (reconnaissance) aracıdır. Modern siber güvenlik süreçlerinde bilgi toplama aşamasının en temel yapı taşlarından birini temsil eder.

✨ Özellikler
Hızlı Port Keşfi: Python'ın socket kütüphanesi ve optimize edilmiş zaman aşımları (0.5s timeout) ile yüksek hızlı tarama performansı.

Servis Tanımlama (Banner Grabbing): Açık bulunan portlarda çalışan yaygın servisleri (SSH, HTTP, FTP, MySQL, vb.) otomatik olarak eşleştirir.

Hata Yönetimi: Geçersiz IP adresleri, çözülemeyen domainler ve kullanıcı müdahalelerine (KeyboardInterrupt) karşı dayanıklı yapı.

Şık Terminal Çıktısı: Tarama başlangıç zamanı, hedef host bilgisi ve açık port listesini temiz ve okunabilir bir formatta sunar.

🚀 Kurulum ve Kullanım
Depoyu Klonlayın:

Dizine Geçiş Yapın:

Aracı Çalıştırın:

İnteraktif Mod: python3 scanner.py yazıp hedef IP'yi sorulduğunda girin.

Hızlı Mod: python3 scanner.py <hedef-ip-veya-domain>

⚙️ Teknik Detaylar
Araç, TCP üçlü el sıkışma (three-way handshake) mantığını simüle ederek hedefe bağlantı isteği gönderir. connect_ex metodu kullanılarak portun durumu analiz edilir:

Dönen Değer 0: Port açık ve bağlantı kabul ediyor.

Diğer Değerler: Port kapalı veya erişilemez.

⚠️ YASAL UYARI VE SORUMLULUK REDDİ
DİKKAT: Bu yazılım sadece eğitim ve etik siber güvenlik testleri amacıyla geliştirilmiştir.

Bu aracın, sahibi olmadığınız veya açık rızanız bulunmayan sistemler üzerinde kullanılması yasalara aykırı olabilir ve ağır yaptırımlara yol açabilir.

Yazılımın kullanımından doğabilecek her türlü yasal sorumluluk tamamen son kullanıcıya aittir.

Geliştirici (Burak), bu aracın kötüye kullanımından veya hedef sistemlerde oluşabilecek olası kesintilerden/hasarlardan dolayı hiçbir sorumluluk kabul etmez.

Bu aracı kullanarak, yukarıdaki şartları ve kullanım koşullarını kabul etmiş sayılarsınız.
