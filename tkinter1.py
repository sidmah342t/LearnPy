from tkinter import *

root = Tk()

newFrame = Frame(root)
newFrame.pack(side=TOP)

otherFrame = Frame(root)
otherFrame.pack(side=BOTTOM)

button1 = Button(newFrame, text="click here", fg="Red")
button2 = Button(otherFrame, text="click here", fg="Blue")

# add buttons to the window
button1.pack()
button2.pack()


root.mainloop()