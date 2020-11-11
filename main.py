import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import sys
from crypts import crypt

LARGE_FONT = ("Verdana", 12)

params_list = []


def inf():
    info_str = 'Программа шифратор/дешифратор.\nСоздана совместно студентами группы 3-ОТЗИ-1К НРТК\nКоровкин ' \
               'Михаил\nКорняков Сергей\nЛебедь Дмитрий\nв 2020 году '
    messagebox.showinfo(title='Информация о программе', message=info_str)


def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    text = f.read()
    f.close()
    return text


def extract_text(text):
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    f = open(file_name, 'w')
    f.write(text)
    f.close()


def main_function():
    return crypt(params_list)


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="Exit", underline=1, command=self.quit)

        help_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", underline=0, menu=help_menu)
        help_menu.add_command(label="About", underline=1, command=inf)

    def quit(self):
        sys.exit(0)


class MyProgram(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        menubar = MenuBar(self)
        self.config(menu=menubar)

        self.title('Шифратор 3000')
        self.geometry('700x400')

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Выберите шифр:", font=LARGE_FONT)
        label.place(x=20, y=20)

        f_v = StringVar()
        f_v.set("permutation")

        cipher_values = [
            ("Транспонирование", "permutation"),
            ("Перестановка рядов", "row_permutation"),
            ("Перестановка столбцов", "column_permutation"),
            ("Шифр Цезаря(шаг и ключ)", "caesar"),
            ("Шифр Цезаря (смещение по y)", "caesar_y"),
            ("Цезарь (смещение по xy) (beta)", "caesar_xy")
        ]

        var = 0
        for txt, value in cipher_values:
            Radiobutton(self, text=txt, variable=f_v,
                        font=LARGE_FONT, bd='5', highlightthickness='0',
                        width=len(txt), value=value).place(x=20, y=40 + (var * 30))
            var += 1

        action_choice = [
            ("Зашифровать", "encrypt"),
            ("Расшифровать", "decrypt")
        ]

        s_title = tk.Label(self, text='Выберите действие:', font=LARGE_FONT)
        s_title.place(x=350, y=20)

        s_v = StringVar()
        s_v.set("encrypt")

        var = 0
        for txt, value in action_choice:
            Radiobutton(self, text=txt, variable=s_v,
                        font=LARGE_FONT, bd='5', highlightthickness='0',
                        width=len(txt), value=value).place(x=350, y=50 + (var * 30))
            var += 1

        def btn_click():
            for i in f_v, s_v:
                params_list.append(i.get())
            controller.show_frame(SecondPage)

        button = tk.Button(self, text="Продолжить", command=btn_click)
        button.place(x=350, y=300)


class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Ввод текста
        label = tk.Label(self, text="Введите текст:", font=LARGE_FONT)
        label.place(x=20, y=0)

        text_field = Text(self, width=80, height=4)
        text_field.place(x=20, y=30)

        def btn_text_insert():
            text_field.insert(1.0, insert_text())

        button_text = tk.Button(self, text='Из файла',
                                command=btn_text_insert)
        button_text.place(x=550, y=110)

        # Ввод ключа
        label = tk.Label(self, text="Введите (если требуется) числовой ключ:", font=LARGE_FONT)
        label.place(x=20, y=120)

        pass_field = Entry(self, bg='white', width=24)
        pass_field.place(x=20, y=150)

        def btn_key_insert():
            pass_field.insert(1, insert_text())

        button_key = tk.Button(self, text='Из файла',
                               command=btn_key_insert)
        button_key.place(x=240, y=145)

        # Ввод второго ключа
        label = tk.Label(self, text="Введите (если требуется) ключ-слово:", font=LARGE_FONT)
        label.place(x=20, y=190)

        pass2_field = Entry(self, bg='white', width=40)
        pass2_field.place(x=20, y=220)

        def btn_key2_insert():
            pass2_field.insert(1, insert_text())

        button_key2 = tk.Button(self, text='Из файла',
                                command=btn_key2_insert)
        button_key2.place(x=370, y=215)

        # Ввод третьего ключа
        label = tk.Label(self, text="Введите (если требуется) третий ключ (алфавит):", font=LARGE_FONT)
        label.place(x=20, y=250)

        pass3_field = Entry(self, bg='white', width=40)
        pass3_field.place(x=20, y=280)
        pass3_field.insert(1, 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

        def btn_key3_insert():
            pass3_field.insert(1, insert_text())

        button_key3 = tk.Button(self, text='Из файла',
                                command=btn_key3_insert)
        button_key3.place(x=370, y=275)

        # Кнопки действий
        def back():
            params_list.clear()
            controller.show_frame(FirstPage)

        button1 = tk.Button(self, text="Вернуться назад",
                            command=back)
        button1.place(x=50, y=360)

        def btn_click():
            params_list.append(text_field.get(1.0, END))
            for i in pass_field, pass2_field, pass3_field:
                params_list.append(i.get())
            print(params_list)

            controller.show_frame(ThirdPage)

        button2 = tk.Button(self, text="Выполнить",
                            command=btn_click)
        button2.place(x=550, y=360)


class ThirdPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        output_text_field = Text(self, width=80, height=4)
        output_text_field.place(x=20, y=30)

        def output_field():
            output_text_field.insert(1.0, main_function())

        button_field = tk.Button(self, text="Вывести результат в текстовое поле",
                                 command=output_field)
        button_field.place(x=20, y=120)

        def output_file():
            extract_text(main_function())

        button_file = tk.Button(self, text="Вывести результат в файл",
                                command=output_file)
        button_file.place(x=450, y=120)

        def back():
            params_list.clear()
            output_text_field.delete(1.0, END)
            controller.show_frame(FirstPage)

        button = tk.Button(self, text="В начало",
                           command=back)
        button.place(x=330, y=330)


app = MyProgram()
app.mainloop()
