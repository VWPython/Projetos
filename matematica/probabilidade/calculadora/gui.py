"""
Interface gráfica para o GUI

Instalação: sudo apt-get intall python3-tk

Tutoriais:
    https://www.tutorialspoint.com/python/python_gui_programming.htm
    http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
"""

from functools import partial
from tkinter import Tk, Label, Button, Entry, Frame, LEFT, PhotoImage, END


class Calculator(object):
    """
    Class that create statistical calculator GUI
    """

    def __init__(self, window):
        self.window = window
        self.__configure_window()
        self.__create_math_label()
        self.__create_input()
        self.__create_calculate_button()
        self.__create_result_label()
        self.__create_math_buttons()

    def __str__(self):
        return "Calculator GUI"

    def __configure_window(self):
        HEIGHT = 600
        WIDTH = 800

        # Give a title to window
        self.window.title("Calculadora Cientifica")

        # Give a size to window
        self.window.geometry("{0}x{1}".format(WIDTH, HEIGHT))

        # Configure color palette and font style
        self.__color_palette()
        self.__font_style()

        # Frame not resizable no x, y
        self.window.resizable(False, False)

        # Background color
        self.window['background'] = self.teal

    def __color_palette(self):
        self.teal_lighten = "#E0F2F1"
        self.teal = "#009688"
        self.teal_darken = "#004D40"
        self.red_darken = "#B71C1C"
        self.black = "black"
        self.white = "white"

    def __font_style(self):
        self.verdana14bold = ('Verdana', '14', 'bold')
        self.verdana10bold = ('Verdana', '10', 'bold')
        self.verdana18bold = ('Verdana', '18', 'bold')

    def __create_math_label(self):
        # Create a welcome label frame
        frame = Frame(self.window)
        frame.pack()

        # Create the math label
        self.math_label = Label(
            frame,
            height=200,
            background=self.teal,
            pady=5
        )
        self.math_label.pack()

        # Create a math label
        logo = PhotoImage(file='img/background.gif')
        self.math_label.image = logo
        self.math_label['image'] = logo

    def __message(self, text, color='#B71C1C'):
        self.result_label['text'] = text
        self.result_label['foreground'] = color

    def __create_input(self):
        # Create a input frame
        frame = Frame(self.window, pady=5, background=self.teal)
        frame.pack()

        # Create the input text
        self.entry_input = Entry(frame, width=50)
        self.entry_input.pack()

    def __create_calculate_button(self):
        # Create a calculate button frame
        frame = Frame(self.window, pady=5, background=self.teal)
        frame.pack()

        # Create calculate button
        self.calculate_button = Button(
            frame,
            text="Calcule",
            foreground=self.white,
            background=self.teal_darken,
            font=self.verdana18bold,
            command=self.__calcule
        )
        self.calculate_button.pack()

    def __calcule(self):
        START = 0

        if self.entry_input.get() == '':
            self.__message("Campo vazio!", self.white)
        else:
            self.__message(self.entry_input.get(), self.white)
            self.entry_input.delete(START, END)

        self.result_label['font'] = self.verdana14bold

    def __create_result_label(self):
        # Create a result label frame
        frame = Frame(self.window, pady=10, background=self.teal)
        frame.pack()

        # Create a result label
        self.result_label = Label(
            frame,
            text="Resultado",
            font=self.verdana14bold,
            background=self.teal,
            foreground=self.white
        )
        self.result_label.pack()

    def __create_math_buttons(self):
        # Create a math button frame
        frame = Frame(self.window)
        frame.pack()

        # Button text
        button_text = (
            'Comb(n, k)',
            'binomial(n, x, p)',
            'poisson(l, x, t)',
            'soma(n, p, maior, menor=0)',
            'media',
            'desvio',
            'moda',
            'mediana',
            'variancia',
            'p(x > k)',
            'p(x >= k)',
            'p(x < k)',
            'p(x <=k)',
            'p(k1 < x < k2)',
            'p(k1 <= x < k2)',
            'p(k1 < x <= k2)',
            'p(k1 <= x <= k2)'
        )

        # Create all subframes with three math button each
        for index in range(len(button_text)):
            if index % 3 == 0:
                subframe = Frame(frame)
                subframe.pack()

            self.math_button = Button(
                subframe,
                text=button_text[index],
                font=self.verdana10bold,
                foreground=self.white,
                background=self.teal_darken,
                width=25,
                command=partial(
                    self.__insert_text_on_input,
                    button_text[index]
                )
            )
            self.math_button.pack(side=LEFT)

        # Create delete button
        self.delete_math_button = Button(
            subframe,
            text="delete",
            font=self.verdana10bold,
            foreground=self.white,
            background=self.red_darken,
            width=25,
            command=self.__delete_text_on_input
        )
        self.delete_math_button.pack()

    def __insert_text_on_input(self, text):
        self.entry_input.insert(END, text)

    def __delete_text_on_input(self):
        self.entry_input.delete(0, END)

if __name__ == '__main__':
    # Create my window
    window = Tk()

    # Create cientific calculator
    Calculator(window)

    # Run GUI
    window.mainloop()
