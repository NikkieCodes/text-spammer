from time import sleep
from tkinter import *

from pynput.keyboard import Controller, Key

kb = Controller()

def main():
    win = Tk()
    win.title("Spammer");win.config(bg='midnight blue')
    win.geometry('300x200');win.resizable(0,0)

    amount = Entry(win,)
    amount.insert(END, "5")
    interval = Entry(win,)
    interval.insert(END, '0.05')
    text = Entry(win,)
    label = Label(win, text="How often: ", bg='midnight blue', fg='white')
    label1 = Label(win, text="Text: ", bg='midnight blue', fg='white')
    label2 = Label(win, text="Interval: ", bg='midnight blue', fg='white')
    amount.place(x=80, y=10)
    text.place(x=80, y=40)
    interval.place(x=80, y=70)
    label.place(x=10,y=10)
    label1.place(x=10, y=40)
    label2.place(x=10, y=70)

    def spam():
        sleep(3)
        amount_int=int(amount.get())
        interval_float=float(interval.get())
        for number in range(amount_int):
            sleep(interval_float)
            kb.type(text.get())
            sleep(0.05)
            kb.press(Key.enter)

    button = Button(win, text="Start", command=spam, width=16)
    button.place(x=80,y=150)

    win.mainloop()

main()
