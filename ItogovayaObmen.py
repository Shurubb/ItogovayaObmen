from pydoc import resolve

import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

from Scripts.pythonProject.venv.Scripts.bottle import response


def exchange():
    code = entry.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс:  {exchange_rate:.2f} {code} за 1 доллар')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Error', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Attention!', 'Введите код валюты')


window = Tk()
window.title('Курсы обмена валют')
window.geometry('150x150')
Label(text='Введите код валюты').pack(pax=10, pady=10)
entry = Entry()
window.mainloop()
