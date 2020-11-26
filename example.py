from tr_topicter import TrTopicter

instance = TrTopicter()

print(instance.get_topic("""
Epidemiyoloji:HIV infeksiyonu ile birlikte dünyada Tbc olgularında artış görülmüştür.
İnfeksiyon hastalıkları içerisinde morbidite ve mortalitesi en yüksek olandır. 
Kişide infeksiyona yatkınlıkbulaşmada önemlidir (genetik faktörler).
Mycobacteria tuberculosis aside dirençli bir bakteri olup Ehrlich-Ziehl-Neelsen boyama yöntemi ilemavi bir 
zemin üzerinde kırmızı çomaklar halinde görülür.Deri tüberkülozu:Deride M tuberculosis, M bovis ve 
bazı durumlarda Bacillus Calmette-Guerin (BCG) infeksiyona neden olur. Tbc yaygın görülmekle beraber etkenler ne 
çok virülandır ne de infeksiyözdür. M. tuberculosis infeksiyonunun ancak %5-10‟u hastalık yapar. 
M tuberculosis dokuda latent bir şekilde kalabilir, tedaviye yanıt vermez ve reaktivasyon gösterebilir"""))

print(instance.get_topic("""
Salgından etkilenen altının gram fiyatı, güne yükselişle başlamasının ardından 473,8 liradan işlem görüyor. 
Aynı dakikalarda çeyrek altın 775 lira, Cumhuriyet altını da 3.163 liradan satılıyor.
Dün, altının ons fiyatı ve dolar kurundaki düşüşe paralel değer kaybeden gram altın, 
günü bir önceki kapanışın yüzde 7,7 altında 468 liradan tamamladı.
SALGIN ALTININ ONS FİYATINI ETKİLİYOR
Gram altın, yeni güne değer kazancıyla başlamasının ardından saat 10.55 itibarıyla önceki kapanışın 
yüzde 1,2 üzerinde 473,8 liradan işlem görüyor. Aynı dakikalarda çeyrek altın 775 lira, 
Cumhuriyet altını da 3.163 liradan satılıyor.
"""))

print(instance.get_topic("""
Onlar yıllardır yeşil sahalarda sergiledikleri futbolla tuttuğumuz takımları galibiyete taşıyor,
Milli takımla bizleri temsil ediyor. Ancak dediğimiz gibi yıllardı. Yıllardır Süper Lig'de 
izlediğimiz futbolcuların gençlik zamanları ve şimdiki halleri arasındaki değişimleri sizi
çok şaşırtacak. A Milli Futbol Takımı'nın UEFA Uluslar B Ligi 3. Grup'ta 18 Kasım Çarşamba
günü Macaristan ile deplasmanda oynayacağı maçı Slovak hakem Ivan Kruzliak yönetecek.
Türkiye Futbol Federasyonunun internet sitesinde yer alan açıklamaya göre, 
başkent Budapeşte'deki Puşkaş Arena'da TSİ 22.45'te başlayacak karşılaşmada düdük çalacak 
Kruzliak'ın yardımcılıklarını Tomas Somolani ve Branislav Hancko yapacak.
Karşılaşmanın dördüncü hakemi ise Filip Glova olacak.
"""))
