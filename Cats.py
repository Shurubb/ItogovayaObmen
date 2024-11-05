import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb



def get_image(url_api):
    try:
        answer = requests.get(url_api)
        image = BytesIO(answer.content)
        img = Image.open(image)
        img.thumbnail((500,450))
        img_tk = ImageTk.PhotoImage(img)
        return img_tk
    except Exception as e:
        mb.showerror('Ошибка', f'Ошибка {e}')
        return None

def set_image():
    img = get_image(url)
    if img:
        new_window = Toplevel()
        new_window.title('Котики')
        new_window.geometry('500x540')
        l = Label(new_window, image=img)
        l.image = img
        l.pack()


def exit_win():
    window.destroy()

url = 'https://cataas.com/cat'

window = Tk()
window.geometry('300x200')
window.title('Гланвое окно')

main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Файл', menu=file_menu)

file_menu.add_command(label='Получить котика', command=set_image)
file_menu.add_separator()
file_menu.add_command(label='Выйти', command=exit_win)



window.mainloop()