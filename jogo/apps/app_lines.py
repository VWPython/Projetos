from tkinter import *

X = 0
Y = 1
INITIAL_X = 200
INITIAL_Y = 200
MOVEMENT = 10


class Lines:
    """
    Inicia o primeiro aplicativo com o canvas que é responsavel
    por desenhar algo utilizando linhas
    """

    def __init__(self, window):
        window.title('Linhas')

        self.canvas = Canvas(
            window,
            width=400,
            height=400,
            cursor='watch',
            background="ghostwhite"
        )
        self.canvas.pack()

        self.frame = Frame(window)
        self.frame.pack()

        self.last_point = [INITIAL_X, INITIAL_Y]

        configs = {
            'foreground': 'white',
            'background': 'black',
            'relief': GROOVE,
            'width': 11,
            'font': ('Verdana', '8', 'bold')
        }

        self.button_left = Button(
            self.frame,
            configs,
            text='Esquerda',
            command=self.left
        )
        self.button_left.pack(side=LEFT)

        self.button_up = Button(
            self.frame,
            configs,
            text='Para cima',
            command=self.up
        )
        self.button_up.pack(side=LEFT)

        self.button_right = Button(
            self.frame,
            configs,
            text='Direita',
            command=self.right
        )
        self.button_right.pack(side=LEFT)

        self.button_down = Button(
            self.frame,
            configs,
            text='Para baixo',
            command=self.down
        )
        self.button_down.pack(side=LEFT)

    def left(self):
        """
        Desenha um segmento de reta para a esquerda
        """

        x = self.last_point[X] - MOVEMENT
        y = self.last_point[Y]

        self.canvas.create_line(self.last_point, x, y, fill='red')

        self.last_point = [x, y]

    def up(self):
        """
        Desenha um segmento de reta para cima
        """

        x = self.last_point[X]
        y = self.last_point[Y] - MOVEMENT

        self.canvas.create_line(self.last_point, x, y, fill='green')

        self.last_point = [x, y]

    def down(self):
        """
        Desenha um segmento de reta para baixo
        """

        x = self.last_point[X]
        y = self.last_point[Y] + MOVEMENT

        self.canvas.create_line(self.last_point, x, y, fill='blue')

        self.last_point = [x, y]

    def right(self):
        """
        Desenha um segmento de reta para a direita
        """

        x = self.last_point[X] + MOVEMENT
        y = self.last_point[Y]

        self.canvas.create_line(self.last_point, x, y, fill='purple')

        self.last_point = [x, y]

if __name__ == '__main__':
    window = Tk()
    Lines(window)
    window.mainloop()
