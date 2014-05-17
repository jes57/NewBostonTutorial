# Simple GUI

from tkinter import *

# Create the window
main_window = Tk()

# Modify main_window window
main_window.title("Labeler")
main_window.geometry("400x200")

# Creates the frame
frame = Frame(main_window)
frame.grid()      # Add the frame to the window

button1 = Button(frame, text = "Button 1")
button1.grid()

# Add text through the configure option
button2 = Button(frame)
button2.grid()
button2.configure(text = "Button 2")

# Add text in dictionary like fashion
button3 = Button(frame)
button3.grid()
button3["text"] = "Button 3"

# Kick off the event loop
main_window.mainloop()
