import supervisor
import terminalio, board
import analogio import AnalogIn
from adafruit_display_text import label

#TODO: get text from sd card

display = supervisor.runtime.display
text = "This is a placeholder. This text will be changed."
#for ease of access. I'll probably tweak this when I actually have the project assembled.
maxchar= 20
scrolllabel = label(terminalio.FONT, text= text, maxcharacters=maxchar, animate_time=0.3)
#make sure to change the A1 to the boards specific value
pot = AnalogIn(board.A1)
#to get it to scroll with the potentiometer, connect these variables to whatever value you get from the pots. (normalize the result as well)
scrolllabel.x = 0
scrolllabel.y = pot.value
display.root_group = scrolllabel
display.autorefresh = False
display.refresh()
while True:
     if scrolllabel.update():
          display.refresh()