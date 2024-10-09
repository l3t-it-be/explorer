import os
import tkinter
from tkinter import filedialog

window = tkinter.Tk()

foldername = ''


def file_selector():
    filename = filedialog.askopenfilename(
        initialdir='/',
        title='Выберите файл: ',
        filetypes=(('Текстовый файл', '*.txt'), ('Все файлы', '*.*')),
    )
    text['text'] = 'Файл: ' + filename
    os.startfile(filename)


def folder_selector():
    global foldername
    foldername = filedialog.askdirectory(initialdir='/')
    text['text'] = 'Папка: ' + foldername
    update_file_list(foldername)


def update_file_list(folder):
    file_listbox.delete(0, tkinter.END)
    for file in os.listdir(folder):
        file_listbox.insert(tkinter.END, file)


def open_selected_file():
    selected_file = file_listbox.get(file_listbox.curselection())
    os.startfile(os.path.join(foldername, selected_file))


window.title('Проводник')
window.geometry('550x300')
window.resizable(False, False)
window.configure(bg='light blue')

text = tkinter.Label(
    window,
    text='Путь к файлу / папке',
    background='dark gray',
    foreground='blue',
    height=1,
    font=('Roboto', 9, 'bold'),
)
text.grid(column=0, row=0, sticky='nsew')

button_select = tkinter.Button(
    window,
    text='Выберите файл',
    command=file_selector,
    height=1,
    foreground='blue',
    font=('Roboto', 9, 'bold'),
)
button_select.grid(column=0, row=1, sticky='ew', padx=0, pady=(10, 5))

button_select_folder = tkinter.Button(
    window,
    text='Выберите папку',
    command=folder_selector,
    height=1,
    foreground='blue',
    font=('Roboto', 9, 'bold'),
)
button_select_folder.grid(
    column=0, row=2, sticky='ew', padx=0, pady=(2, 5)  # Уменьшен нижний отступ
)

file_listbox = tkinter.Listbox(window, height=10, width=50)
file_listbox.grid(column=0, row=3, sticky='nsew', padx=10, pady=(5, 10))
file_listbox.bind('<Double-1>', lambda event: open_selected_file())


window.grid_rowconfigure(0, weight=3)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=5)
window.grid_columnconfigure(0, weight=2)

window.mainloop()
