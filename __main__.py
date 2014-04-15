import tkinter as tk
from src import run

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = tk.Entry(self, width=590)
        self.input.pack()

        self.add = tk.Button(self, text="dodaj", command=self.get_url)
        self.add.pack()

    def get_url(self):
        run(self.input.get())


root = tk.Tk()
app = Application(master=root)
app.master.minsize(700, 50)
app.master.maxsize(700, 50)
app.mainloop()