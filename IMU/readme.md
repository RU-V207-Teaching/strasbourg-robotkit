Testing procedure for the non-branded Adafruit 9-DOF board
https://www.adafruit.com/product/1032

STMicro L3G4200D 3-axis gyroscope
Pololu overview page:  https://www.pololu.com/product/1272
Datasheet:  https://www.pololu.com/file/0J491/L3G4200D.pdf
Arduino Lib: https://github.com/adafruit/Adafruit_L3GD20_U
Python support:  https://www.pololu.com/file/0J491/L3G4200D.pdf

STMicro LSM303D-TR  3D Accelerometer + 3D Compass
Adafruit guide (different board) https://learn.adafruit.com/lsm303-accelerometer-slash-compass-breakout/python-circuitpython
STMicroelectronics reference:  https://www.st.com/en/mems-and-sensors/lsm303d.html

Testing configuration:
Materials:  Adafruit Metro M4 Airlift Lite  (Firmware ??, MicroPython ??, Bootload ??)

Wire these pins together  (notice that some do not get wired)
```
Metro	9DOF board
3v3 --> Vin
--- --> 3V0
GND --> GND
SCL --> SCL 
SDA --> SDA
--- --> GINT
--- --> GRDY
--- --> LIN1
--- --> LIN2
--- --> LRDY
```

Copy all the files that start "adafruit" and end in .mpy into lib on CIRCUITPY drive.  These are stock versions from the bundle 8.x at https://circuitpython.org/libraries

Copy l3g4200d.py and l3g4200d-gyro_test.py on to the CIRCUITPY drive.  Rename l3g4200d-gyro_test.py to code.py
Open Mu (or other) serial console at 115200 baud
Rotating it should see some change in the numbers.

Copy lsm303-accel_test.py and rename to code.py
Open Mu (or other) serial console at 115200 baud
Tilting it should see one of the numbers go up or down

Copy lsm303dlh-mag_test and rename to code.py
Open Mu (or other) serial console at 115200 baud
Bringing a magnet nearby or rotating should change numbers

WARNING: Included Gyro uses a different I2C address (0x69) and has different Chip Id (0XD3) which will cause the libraries provided to break.  We are figuring out what the best workaround is.
You can make this work by recompiling the related library, but we don't recommend that because then if you reinstall the stock library everything will break.
Copy l3gd20-gyro_test.py and rename to code.py
Open Mu (or other) serial console at 115200 baud
Shaking it should see some movement
