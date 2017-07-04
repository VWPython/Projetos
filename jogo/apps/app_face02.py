from tkinter import *

MOVEMENT = 10


class Face02:
    def __init__(self, window):
        self.window = window
        self.window.title('Carinha 2')

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

        # Pega o evento de clique das setas do teclado
        self.canvas.bind('<Left>', self.left)
        self.canvas.bind('<Right>', self.right)
        self.canvas.bind('<Up>', self.up)
        self.canvas.bind('<Down>', self.down)

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

    def left(self, event): self.canvas.move('bola', -MOVEMENT, 0)

    def right(self, event): self.canvas.move('bola', MOVEMENT, 0)

    def up(self, event): self.canvas.move('bola', 0, -MOVEMENT)

    def down(self, event): self.canvas.move('bola', 0, MOVEMENT)

if __name__ == '__main__':
    window = Tk()
    Face02(window)
    window.mainloop()
