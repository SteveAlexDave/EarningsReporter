import tkinter as tk


window = tk.Tk()

greeting = tk.Label(text="Hello")

#pack will put widget in window and resize window as small as possible to still contain widget
greeting.pack()


window.mainloop()
