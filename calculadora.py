import tkinter as tk
#from tkinter import messagebox

root = tk.Tk()

root.title("Practica 3")
root.config(width=300, height=330)
#print(root.winfo_screenheight())
#print(root.winfo_screenwidth())

btn1 = tk.Button(root, text="1", width=10, height=5)
btn2 = tk.Button(root, text="2", width=10, height=5)
btn3 = tk.Button(root, text="3", width=10, height=5)
btn4 = tk.Button(root, text="4", width=10, height=5)
btn5 = tk.Button(root, text="5", width=10, height=5)
btn6 = tk.Button(root, text="6", width=10, height=5)
btn7 = tk.Button(root, text="7", width=10, height=5)
btn8 = tk.Button(root, text="8", width=10, height=5)
btn9 = tk.Button(root, text="9", width=10, height=5)

btn1.place(x=0, y=75)
btn2.place(x=80, y=75)
btn3.place(x=160, y=75)
btn4.place(x=0, y=160)
btn7.place(x=0, y=245)

root.mainloop()
