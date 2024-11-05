from tkinter.ttk import Combobox

import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def up_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)

def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name= cur[code]
                mb.showinfo('Курс обмена', f'Курс:  {exchange_rate:.2f} {c_name} за 1 доллар')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Error', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Attention!', 'Введите код валюты')

cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'CNY': 'Китайский юань',
    'GBP': 'Фунт стерлингов',
    'JPY': 'Японская йена',
    'UZS': 'Узбекский сум',
    'KZT': 'Казахский тенге',
    'AED': 'Арабский дирхам',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк'
}

window = Tk()
window.title('Курсы обмена валют')
window.geometry('250x200')
Label(text='Выберите код валюты').pack(padx=10, pady=10)

combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx = 10, pady = 10)
combobox.bind('<<ComboboxSelected>>', up_c_label)
c_label = ttk.Label()
c_label.pack(padx=10, pady=10)
Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()
