from tkinter import *
NUM_IMAGENS = 4


def separate_unique_image(image, x1, y1, x2, y2):
    """
    Com essa função, se tivessemos uma imagem única
    poderíamos separar cada uma das imagens
    por meio dela
    """

    dst = PhotoImage()
    dst.tk.call(dst, 'copy', image, '-from', x1, y1, x2, y2, '-to', 0, 0)
    return dst


def get_separated_image():
    """
    Para o caso de uma imagem única com todas
    as sprites dentro poderíamos extraí-las dessa forma
    """

    self.imagens = []
    for i in range(4):
        sub_image = separate_unique_imagem(
            self.spritesheet,
            i*28,
            0,
            (i+1)*28,
            18
        )
        self.imagens.append(sub_image)


class Mario:

    def __init__(self, window):
        self.window = window
        self.window.title('Mario')

        # Primeiro abrimos o spritesheet
        self.spritesheet = []
        sheet1 = []
        sheet2 = []
        for i in range(1, 5):
            sheet1.append(PhotoImage(file='img/mario/mario_%i.ppm' % i))
            sheet2.append(PhotoImage(file='img/mario/mario_l%i.ppm' % i))

        self.spritesheet.append(sheet1)
        self.spritesheet.append(sheet2)

        # Variavel que contem o número da imagem
        self.image_number = 3
        self.limit = 0

        # Colocamos a posição do mario
        self.x = 100
        self.y = 71
        self.p = False
        self.m_vx = 10
        self.vx = 0
        self.d = 0
        self.moveu = True

        # Configuramos o canvas
        self.canvas = Canvas(
            self.window,
            height=100,
            width=200,
            takefocus=1,
            background='black',
            highlightthickness=0
        )
        self.canvas.bind('<Left>', self.left)
        self.canvas.bind("<KeyRelease-Left>", self.solta)
        self.canvas.bind("<KeyRelease-Right>", self.solta)
        self.canvas.bind('<Right>', self.right)
        self.canvas.focus_force()
        self.canvas.pack()

        # Colocamos um botão para começar o jogo
        self.start_button = Button(
            self.window,
            text='START',
            command=self.start
        )
        self.start_button.focus_force()
        self.start_button.pack()

        self.window.mainloop()

    def left(self, event):
        """
        Move o personagem para a esquerda
        """

        self.vx = -self.m_vx
        self.d = 1
        self.p = True

    def right(self, event):
        """
        Move o personagem para a direita
        """

        self.vx = self.m_vx
        self.d = 0
        self.p = True

    def solta(self, event):
        self.p = False

    def start(self):
        """
        Inicia o jogo
        """

        self.walk()

    def walk(self):
        """
        Deve ser executado enquanto o jogo estiver rodando
        """

        if self.p:

            if 0 < self.x < 184:
                self.x += self.vx

            if self.x > 184:
                self.x = 183

            if self.x < 16:
                self.x = 17

            self.image_number -= 1

            if self.image_number < 0:
                self.image_number = 3

        else:
            self.image_number = 3

        self.canvas.delete(ALL)

        self.canvas.focus_force()

        self.canvas.create_image(
            (self.x, self.y),
            image=self.spritesheet[self.d][self.image_number]
        )

        self.window.after(70, self.walk)

    def draw(self):
        self.image_number += 1


if __name__ == '__main__':
    window = Tk()
    Mario(window)
