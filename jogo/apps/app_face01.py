from tkinter import *


class Face01:

    def __init__(self, window):
        self.window = window
        self.window.title('Carinha')

        self.canvas = Canvas(
            self.window,
            height=200,
            width=200,
            takefocus=1,
            background='deepskyblue',
            highlightthickness=0
        )
        self.canvas.focus_force()
        self.canvas.pack()

        # Desenha o circulo amarealo que será a carinha (x0, y0, x1, y1)
        # x0 e y0 = ponto acima e a esquerda
        # x1 e y1 = ponto a direita e abaixo
        self.canvas.create_oval(
            90, 90, 110, 110,
            tag='bola',
            fill='yellow'
        )

        # Desenha o olho esquerdo da carinha (x0, y0, x1, y1)
        # x0 e y0 = ponto acima e a esquerda
        # x1 e y1 = ponto a direita e abaixo
        self.canvas.create_oval(
            93, 100, 98, 95,
            tag='bola',
            fill='blue'
        )

        # Desenha o olho direito da carinha (x0, y0, x1, y1)
        # x0 e y0 = ponto acima e a esquerda
        # x1 e y1 = ponto a direita e abaixo
        self.canvas.create_oval(
            102, 100, 107, 95,
            tag='bola',
            fill='blue'
        )

        # Desenha a boca da carinha através de um arco (x0, y0, x1, y1)
        # x0 e y0 = ponto acima e a esquerda
        # x1 e y1 = ponto a direita e abaixo
        self.canvas.create_arc(
            92, 87, 108, 107,
            tag='bola',
            start=220,
            extent=100,
            style=ARC
        )

        self.vx = 5
        self.vy = 4
        self.x = 90
        self.y = 90

        # Colocamos um botão para começar o jogo
        self.start_button = Button(
            self.window,
            text='START',
            command=self.start
        )
        self.start_button.pack()

    def start(self):
        self.move()

    def move(self):
        self.canvas.move('bola', self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy

        if self.x > 180 or self.x < 0:
            self.vx *= -1
        if self.y > 180 or self.y < 0:
            self.vy *= -1

        self.window.after(10, self.move)

if __name__ == '__main__':
    window = Tk()
    Face01(window)
    window.mainloop()
