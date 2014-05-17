# Using a class to access tkinter

from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """

    def __init__(self, master):
        """ Initializes the Frame"""
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0  # count the number of button clicks
        self.create_widgets()

    def create_widgets(self):
        """ Create 3 buttons that displays number of clicks"""
        # Create the first button
        self.button1 = Button(self)
        self.button1["text"] = "Total Clicks: 0"
        self.button1["command"] = self.update_count # Bind event handler
        self.button1.grid()

    def update_count(self):
        """ Increase the click count and display the new total"""
        self.button_clicks += 1
        self.button1["text"] = "Total Clicks: " + str(self.button_clicks)

# Main program functionality        
main_window = Tk()
main_window.title("Lazy buttons")
main_window.geometry("400x200")

# Use Application class in place of Frame class because we overloaded it
app = Application(main_window)

main_window.mainloop()
