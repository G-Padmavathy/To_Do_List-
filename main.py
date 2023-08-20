import pickle
import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog

COLOUR = "#e39ff6"
tkWindow = tk.Tk()
tkWindow.config(bg=COLOUR)
tkWindow.title('ToDo-List')

tkWindow.state("zoomed")

my_font = Font(
    family="lucida calligraphy",
    size=30,
    weight="bold")

my_frame = tk.Frame(tkWindow)
my_frame.pack(pady=10)

my_list = tk.Listbox(my_frame,
                     font=my_font,
                     width=40,
                     height=8,
                     bg="SystemButtonFace",
                     bd=0,
                     fg="#464646",
                     highlightthickness=0,
                     selectbackground="#601a35",
                     activestyle="none")
my_list.pack(side=tk.LEFT, fill=tk.BOTH)

# stuff = ["you can do it keep fight", "don't give up ","jai sri rama", "hare krishna","hare rama","Padmavathy"]
# for item in stuff:
#     my_list.insert(tk.END, item)

my_scrollbar = tk.Scrollbar(my_frame)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry = tk.Entry(tkWindow, font=("helvetica", 20), insertborderwidth=50, width=50)
my_entry.pack(pady=40, padx=40)


button_frame = tk.Frame(tkWindow, background=COLOUR)
button_frame.pack(pady=20)


def delete_item():
    my_list.delete(tk.ANCHOR)


def add_item():
    my_list.insert(tk.END, my_entry.get())
    my_entry.delete(0, tk.END)


def cross_off_item():
    my_list.itemconfig(my_list.curselection(), fg="#7a4988")
    my_list.selection_clear(0, tk.END)


def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    my_list.selection_clear(0, tk.END)


def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#7a4988":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
        file_name = filedialog.asksaveasfilename(
        initialdir=r'C:\Users\HP 850G3\Desktop\material\to-do-list\data',
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
        )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'
            count = 0
            while count < my_list.size():
                if my_list.itemcget(count, "fg") == "#7a4988":
                    my_list.delete(my_list.index(count))
                else:
                    count += 1

            stuff = my_list.get(0, tk.END)
            output_file = open(file_name, 'wb')
            pickle.dump(stuff, output_file)




def open_list():
    file_name = filedialog.askopenfilename(
        initialdir=r'C:\Users\HP 850G3\Desktop\material\to-do-list\data',
        title="open File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
    )
    if file_name:
        my_list.delete(0, tk.END)
        input_file = open(file_name, 'rb')
        stuff = pickle.load(input_file)
        for item in stuff:
            my_list.insert(tk.END, item)



def clear_list():
    my_list.delete(0, tk.END)


my_menu = tk.Menu(tkWindow)
tkWindow.config(menu=my_menu)


file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)


delete_button = tk.Button(button_frame, text="DeleteItem", command=delete_item, background="#e32227")
add_button = tk.Button(button_frame, text="AddItem", command=add_item, background="#337CCF")
cross_off_button = tk.Button(button_frame, text="Cross Off Item", command=cross_off_item, background="#FE7BE5")
uncross_button = tk.Button(button_frame, text="Uncross Item", command=uncross_item, background="#313866")
delete_crossed_button = tk.Button(button_frame, text="Delete Crossed Item", command=delete_crossed, background="#A084E8")

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2, padx=20)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4, padx=20)


tkWindow.mainloop()