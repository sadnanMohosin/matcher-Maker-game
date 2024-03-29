from tkinter import Tk, Button, DISABLED
import random
import time

def show_symbol(x,y):
    global first
    global previous_x,previous_y
    buttons[x,y]['text'] = buttons_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previous_x = x 
        previous_y =  y
        first = False
    elif previous_x !=x or previous_y !=y:
        if buttons[previous_x,previous_y]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previous_x,previous_y]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previous_x,previous_y]['command'] = DISABLED
            buttons[x,y]['command']= DISABLED
        first = True



win = Tk()
win.title("MatchMaker Game")
win.resizable(width = False, height=False)
first  = True
previous_x = 0
previous_y = 0
buttons = {}
buttons_symbols= {}
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command= lambda x=x, y=y: show_symbol(x,y), width = 10 , height = 8)
        button.grid(column =x , row = y)
        buttons[x,y] = button
        buttons_symbols[x,y] = symbols.pop()




win.mainloop()
