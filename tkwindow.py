from tkinter import Entry, Button, Label, Tk, filedialog, END
from convert import file_paths, convert_list

class ConvGUI:
    def __init__(self, master):
        self.master = master
        master.title("Audio converter")

        self.src_label = Label(master, text="Enter source dir path...")
        self.src_label.grid(row=1, column=0)

        self.src_entry = Entry(master, width=80)
        self.src_entry.grid(row=1, column=1)

        self.src_button = Button(master, text="...", command=lambda: self.pick(self.src_entry))
        self.src_button.grid(row=1, column=2)

        self.dst_label = Label(master, text="Enter destination dir path...")
        self.dst_label.grid(row=2, column=0)

        self.dst_entry = Entry(master, width=80)
        self.dst_entry.grid(row=2, column=1)

        self.dst_button = Button(master, text="...", command=lambda: self.pick(self.dst_entry))
        self.dst_button.grid(row=2, column=2)

        self.bitrate_label = Label(master, text="Enter bitrate")
        self.bitrate_label.grid(row=3, column=0)

        self.bitrate_entry = Entry(master, width=4)
        self.bitrate_entry.grid(row=3, column=1)

        self.convert_button = Button(master, text='Convert', command = lambda : self.convert())
        self.convert_button.grid(row=4)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=5)

    def pick(self, entry):
        dir = filedialog.askdirectory()
        entry.delete(0, END)
        entry.insert(0, dir)

    def convert(self):
        paths = file_paths(self.src_entry.get())
        convert_list(paths, self.src_entry.get(), self.dst_entry.get(), self.bitrate_entry.get())


root = Tk()
my_gui = ConvGUI(root)
root.mainloop()
