import json
from importlib.metadata import files
from tkinter import *
import requests as r
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pyperclip
import os


def save_files(path_file, link_file, name_file):
    history = []
    if os.path.exists('History.json'):
        with open('History.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
    history.append({'path_file': path_file, 'name_file': name_file, 'link_file': link_file})
    with open('History.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)



def load_file():
    try:
        file = fd.askopenfilename()
        if file:
            answer = r.post('https://file.io', files={'file': open(file, 'rb')})
            if answer.status_code == 200:
                link_file = answer.json()['link']
                name_file = answer.json()['name']
                e.delete(0, END)
                e.insert(0, link_file)
                pyperclip.copy(link_file)
                save_files(file, link_file, name_file)
            else:
                print('Ошибка')
    except Exception as exc:
        mb.showerror('Ошибка', f'Ошибка: {exc}')


def show_history():
    if not os.path.exists('History.json'):
        mb.showinfo('Внимание','Файла ещё нет')
        return
    else:
        history_window = Toplevel()
        lisf_f = Listbox(history_window)
        lisf_f.pack()

        with open('History.json', 'r') as file:
            hist_link = json.load(file)
            for i in hist_link:
                lisf_f.insert(END, i['link_file'])


window = Tk()
window.title('Обмен файлами')
window.geometry('300x200')

btn= Button(window, text='Загрузить файл в облако', command=load_file)
btn.pack(pady=10)


e = Entry()
e.pack()

btn1= Button(window, text='История загрузок', font=('Arial', 14), command=show_history)
btn1.pack()

window.mainloop()