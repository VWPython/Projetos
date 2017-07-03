"""
Interface gráfica para o GUI

Instalação: sudo apt-get intall python3-tk

Tutoriais:
    https://www.tutorialspoint.com/python/python_gui_programming.htm
    http://effbot.org/tkinterbook/tkinter-index.htm#class-reference
"""

from tkinter import Tk, Label, Button, Entry, Frame, LEFT


class StatisticalCalculator(object):
    """
    Class that create statistical calculator GUI
    """

    def __init__(self, window):
        self.window = window
        self.configure_window()
        self.welcome_label = self.create_label()
        self.entry_input = self.create_input()
        self.calculate_button = self.create_calculate_button()
        self.result_label = self.create_result_label()
        self.create_statistic_buttons()

    def __str__(self):
        return "Statistical calculator GUI"

    def __calcule(self):
        self.result_label['text'] = self.entry_input.get()
        self.result_label['foreground'] = "green"

    def configure_window(self):
        # Give a title to window
        self.window.title("Calculadora para Estatística")

        # Give a size to window
        self.window.geometry("800x600")

    def create_label(self):
        # Create a welcome label frame
        frame = Frame(
            self.window
        )

        # Create the welcome label
        label = Label(
            frame,
            text="Bem vindo!",
            pady=20
        )

        # Packing the frame and label
        frame.pack()
        label.pack()

        return label

    def create_input(self):
        # Create a input frame
        frame = Frame(
            self.window,
            pady=5
        )
        # Create the input text
        entry_input = Entry(
            frame
        )

        # Packing the frame and input
        frame.pack()
        entry_input.pack()

        return entry_input

    def create_calculate_button(self):
        # Create a calculate button frame
        frame = Frame(
            self.window,
            pady=5
        )
        # Create calculate button
        button = Button(
            frame,
            text="Calcule",
            foreground="black",
            background="green",
            command=self.__calcule
        )

        # Packing the frame and button
        button.pack()
        frame.pack()

        return button

    def create_result_label(self):
        # Create a result label frame
        frame = Frame(
            self.window,
            pady=5
        )

        # Create a result label
        label = Label(
            frame,
            text="Resultado",
            foreground="blue"
        )

        # Packing the frame and label
        label.pack()
        frame.pack()

        return label

    def create_statistic_buttons(self):
        # Create a statistic button frame
        frame = Frame(
            self.window
        )

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

        # Create all subframes with three statistic button each
        for index in range(len(button_text)):
            if index % 3 == 0:
                subframe = Frame(frame)
                subframe.pack()
            self.button = Button(
                subframe,
                text=button_text[index],
                background="green",
                width=25
            )
            self.button.pack(side=LEFT)
        frame.pack()

        self.delete_button = Button(
            subframe,
            text="delete",
            background="red",
            width=25
        )
        self.delete_button.pack()

if __name__ == '__main__':
    # Create my window
    window = Tk()

    # Create statistical calculator
    StatisticalCalculator(window)

    # Run GUI
    window.mainloop()
