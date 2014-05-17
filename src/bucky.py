# Simple GUI

from tkinter import *

# Create the window
root = Tk()

# Modify root window
root.title("Labeler")
root.geometry("200x50")

# Creates the frame
app = Frame(root)
app.grid()      # Add the app to the window
label = Label(app, text = "This is a label")
label.grid()    # Add the label to the window


# Kick off the event loop
root.mainloop()
