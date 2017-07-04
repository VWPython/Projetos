from tkinter import *
from time import localtime

class Time:
    def __init__(self,raiz):
        self.canvas=Canvas(raiz, width=200, height=100)
        self.canvas.pack()
        self.frame=Frame(raiz)
        self.frame.pack()
        self.altura = 100 # Altura do canvas

        # Desenho do relógio-----------------------------
        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        self.texto=self.canvas.create_text
        self.fonte=('BankGothic Md BT','20','bold')
        pol(10, self.altura-10, 40, self.altura-90, 160, self.altura-90, 190, self.altura-10, fill='darkblue')
        pol(18, self.altura-15, 45, self.altura-85, 40155, self.altura-85, 182, self.altura-15, fill='dodgerblue')
        ret(45, self.altura-35, 90, self.altura-60, fill='darkblue', outline='')
        ret(110, self.altura-35, 155, self.altura-60, fill='darkblue', outline='')
        self.texto(100, self.altura-50, text=':',font=self.fonte, fill='yellow')
        # Fim do desenho do relógio-----------------------

        self.mostrar=Button(self.frame, text='Que horas são?', command=self.mostra, font=('Comic Sans MS', '11', 'bold'), fg='darkblue', bg='deepskyblue')
        self.mostrar.pack(side=LEFT)

    def mostra(self):
        self.canvas.delete('digitos_HORA')
        self.canvas.delete('digitos_MIN')
        HORA = str( localtime()[3] )
        MINUTO = str( localtime()[4] )
        self.texto(67.5, self.altura-50, text=HORA, fill='yellow',
        font=self.fonte, tag='digitos_HORA')
        self.texto(132.5, self.altura-50, text=MINUTO, fill='yellow', font=self.fonte, tag='digitos_MIN')

if __name__ == '__main__':
    instancia=Tk()
    Horas(instancia)
    instancia.mainloop()
