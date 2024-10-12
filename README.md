## Simple Text Finder Tool for Rokoko .txt Files

**A few words about the .txt files and the tool**
Amongst other information, there is crucial information relative to every sensor's function

This information includes the sensor's Bootloader version, Boot status , Firmware version , Signature , Setup status ,*Calibration ID*, Build number and Hardware version.

The above is categorized by sensor ID.

The specific tool finds the *Calibration ID* with the value *0xfefefefe* and announces to which sensor it belongs to (i.e. Sensor with addr 0x23) and how many times it was found on each sensor

The other function of the specific tool is that it locates on which finger there's been a BMI configuration fail

This is done by locating the string *"BMI configuration fail on finger"* and isolating the number following that string

**Libraries used:**
- sys
- Pandas
- Tkinter (for GUI's creation)


***All rights to the production of the .txt files and the tool's logo go to Rokoko***
