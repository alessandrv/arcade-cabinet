# arcade-cabinet
Files used to build my arcade cabinet


3d printed buttons, 30mm.
Edited OBSMX to work without pcb and have a lower profile. I created 2 different version of the washer to fit 3 rgb pcb to light the keys

The lighting effects will be directed by ledspicer supported by batocera that will run on the host computer. It uses adalight to work, so I used the LEDstream_FastLED arduino project to make an esp32 work with that.

All controls will work because of a raspberry pico clone (YD-2040) runnin GP2040-CE.

Plans to add lightguns running openfire.