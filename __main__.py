import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = tk.Entry(self)
        self.input.pack()

        self.add = tk.Button(self, text="dodaj")
        self.add.pack()


root = tk.Tk()
app = Application(master=root)
app.master.minsize(600, 100)
app.master.maxsize(600, 100)
app.mainloop()