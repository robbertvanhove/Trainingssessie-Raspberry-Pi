# Trainingssessie Raspberry Pi
## 1. Installatie raspbian
Wij hebben voor jullie het besturingssysteem vooraf al geïnstalleerd. Als je dit zelf eens wil uitproberen, kan je volgende handleiding volgen: https://www.raspberrypi.org/documentation/installation/installing-images/README.md

## 2. Raspberry Pi verbinden met je pc
### 1. Verander het IP-adres van je netwerkkaart
* Ga naar configuratiescherm > netwerk en internet > netwerkcentrum
* Klik hier op adapterinstellingen wijzigen

![Adapterinstellingen](adapterinstelling1.png)
* Klik met de rechtermuisknop op de adapter van je ethernet-poort en kies dan eigenschappen

![Adapterinstellingen](adapterinstelling2.png)
* Selecteer vervolgens "Internet Protocol versie 4" en klik op eigenschappen

![Adapterinstellingen](adapterinstelling3.png)
* Kies voor "Het volgende IP-adres gebruiken" en vul vervolgens 192.168.137.1 in als IP-adres en 255.255.255.0 al subnetmasker en klik op "OK"

![Adapterinstellingen](adapterinstelling4.png)
### 2. Deel je Wi-Fi
* Klik met je rechtermuisknop op je wifi-verbinding en kies "eigenschappen"

![Wifi](wifi1.png)
* klik vervolgens op "delen" en vink de eerste checkbox aan

![Wifi](wifi2.png)
### 3. Verbinden met je Raspberry Pi via Putty
* Verbind eerst je pc en je Raspberry Pi via een netwerkkabel
* Open Putty

![Putty](Putty1.png)
* Vul als IP-adres 192.168.137.2 in en zorg er zeker voor dat de poortnummer 22 is.

![Putty](Putty2.png)
* Klik nu op "Open"

![Putty](Putty3.png)
* Vervolgens krijg je een login scherm te zien. Standaard  is de gebruikersnaam "pi" en het wachtwoord "raspberry"

![Putty](Putty4.png)




