# Using a class to access tkinter

from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """

    def __init__(self, master):
        """ Initializes the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create 3 buttons that do nothing"""
        # Create the first button
        self.button1 = Button(self, text = "Button 1")
        self.button1.grid()

        # Second button
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "Button 2")

        # Third button
        self.button3 = Button(self)
        self.button3.grid()
        self.button3["text"] = "Button 3"
main_window = Tk()
main_window.title("Lazy buttons")
main_window.geometry("400x200")

# Use Application class in place of Frame class because we overloaded it
app = Application(main_window)

main_window.mainloop()
