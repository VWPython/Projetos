from tkinter import *

class SPFC:
    def __init__(self,raiz):
        raiz.title('SPFC')
        self.canvas=Canvas(raiz, width=200, height=200, bg='dodgerblue')
        self.canvas.pack()
        
        altura = 200 # Altura do canvas
        
        pol=self.canvas.create_polygon
        
        ret=self.canvas.create_rectangle
        
        pol(100, altura-10, 10, altura-145, 10, altura-190, 190, altura-190, 190, altura-145, 100, altura-10, fill='white')
        
        ret(15, altura-150, 185, altura-185, fill='black')
        
        pol(20, altura-140, 95, altura-140, 95, altura-30, 20, altura-140, fill='red')
        
        pol(105, altura-30, 105, altura-140, 180, altura-140, 105, altura-30, fill='black')
        
        self.canvas.create_text(100, altura-167.5, text='SPFC', font=('Arial','26','bold'), anchor=CENTER, fill='white')

if __name__ == '__main__':
    instancia=Tk()
    SPFC(instancia)
    instancia.mainloop()
