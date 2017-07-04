from tkinter import *


class Draw:

    def __init__(self, window):
        window.title('Desenha')
        self.canvas = Canvas(
            window,
            width=300,
            height=300,
            background='#BEFF8C',
            cursor='hand2'
        )
        # Pega o clique do usuário
        self.canvas.bind('<1>', self.drawing)
        self.canvas.pack()

    def drawing(self, event):
        x_origin = self.canvas.winfo_rootx()
        y_origin = self.canvas.winfo_rooty()
        x_destiny = self.canvas.winfo_pointerx()
        y_destiny = self.canvas.winfo_pointery()
        try:
            point = (x_destiny - x_origin, y_destiny - y_origin)
            self.canvas.create_line(self.last_point, point)
            self.last_point = point
        except:
            self.last_point = (x_destiny - x_origin, y_destiny - y_origin)

if __name__ == '__main__':
    window = Tk()
    Draw(window)
    window.mainloop()
