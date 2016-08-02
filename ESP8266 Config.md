# ESP8266

1- FTDI Kablo Bağlantıları şu şekilde olmalı:

- Red ---> 5V
- Black -> Ground
- White -> Rx
- Green -> Tx

2- NODEMCU ile firmware update yapılması:

FTDI ile bağlarken,
Rx-Tx e
Tx-Rx e bağlanmalı.
3 tane vcc yan yana. sadece Reset pini boşta kalacak.

Ayrıca .bin uzantılı dosyalar seçilmeli, yükleme yapılması için


3- Firmware update sonrasında, Esplorer ile code atılacak:

2 bağlantı çıkarılmalı.
Birincisi 3 tane Vcc bağlı kablonun ortasındaki.

İkincisi Toprağa bağlı olan, GND ucu dışındaki uç

02.08.2016 Gece--> 
a- NodeMCU ile firmware atılabiliyor.

b- ESP8266 LED aç kapa yapabiliyor.

c- TCP üzerinden web server kurulacak!
