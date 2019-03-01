# Program to add, multiply, subtract and divide with a GUI.

#!/usr/bin/python
# main window 
import tkinter
window = tkinter.Tk()
window.title("Calculator")

# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# creating widgets in top frame and bottom 
btn1 = tkinter.Button(top_frame, text = "Button 1", fg = "red").pack() #fg stands for foreground and is used to color the contents 
btn2 = tkinter.Button(top_frame, text = "Button 2", fg = "red").pack() #text is what is written on the button 
btn3 = tkinter.Button(bottom_frame, text = "Button 3", fg = "purple").pack(side = "left") # 'side' is used to allign the widgets
btn4 = tkinter.Button(bottom_frame, text = "Button 4", fg = "purple").pack(side = "left")
                                          
# adding text in window
# label = tkinter.Label(window, text = "Hello world!").pack()

# keeping window open
window.mainloop()
