esp32-projector-controller
=

**Micropython for ESP32 to control a Projector Kodak Carousel S-AV 2060**

This project was done as part of the exhibition
[Vesko Gösel et Adrien Cater](http://www.standard-deluxe.ch/full_content.php?expo=230203_vesko-gosel_adrien-cater)
at [Standard/Deluxe](http://www.standard-deluxe.ch)
in Lausanne, Switzerland.


Installation
-
```
wget https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin
esptool.py --baud 921600 --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --baud 921600 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin

ampy --baud 115200 --port /dev/ttyUSB0 put main.py
ampy --baud 115200 --port /dev/ttyUSB0 put pinout.py
```

Usage
-
Note: `forever()` is called after boot (see [main.py](main.py)).

Connect to ESP32 console:
```
picocom -b 115200 /dev/ttyUSB0
```