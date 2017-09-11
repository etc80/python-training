from tkinter import *


window = Tk()
window.geometry("350x150")
window.title("Data Analyzer")

t1 = Label(window, text="Test Window", fg='grey')
t1.config(font=('Verdana', 25))
t1.pack()

b1 = Button(window, text="Click Me!")
b1.config(width=20, height=2, bg='darkgrey', fg='black')
b1.pack()

window.mainloop()