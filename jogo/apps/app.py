"""
TODO: Arrumar erro que está dando no registro de usuário, por
algum motivo ele acha que o label_name ta usando .grid() e .pack()
ao mesmo tempo
"""

# Importamos o módulo do tkinter
from tkinter import *
from app_lines import Lines
from app_spfc import SPFC
from app_slices import Slices
from app_face01 import Face01
from app_face02 import Face02
from app_mario import Mario
from app_draw import Draw
from app_time import Time

# Importamos o shelve para lidar com o database
import shelve

BLUE = '#3784BA'
NORTH = N
WEST = W
EAST = E
SOUTH = S


class Login(object):
    """
    Classe de autenticação com o sistema
    """

    def __init__(self, window):
        self.window = window
        self.font = ('Verdana', '36', 'bold')

        # Frame principal que contem as entradas de texto
        self.window_frame = Frame(window)
        self.window_frame['background'] = BLUE

        # Frame que contem os botões
        self.button_frame = Frame(window)
        self.button_frame['background'] = BLUE

        self.main_screen()

        # Abrimos os databases com as senhas
        self.database = shelve.open("login.db")

        # Criamos a variável booleana que verifica se estamos no modo registro
        self.create = False

        # Verificamos se devemos preencher os campos de texto com algo
        self.fill_text_input()

        # Empacotamos os widgets
        self.package_main_screen()

    def main_screen(self):
        """
        Cria e empacota os elementos principais do aplicativo
        """

        self.button_image_new = PhotoImage(file='img/button_new.ppm')
        self.button_image_create = PhotoImage(file='img/button_create.ppm')
        logo = PhotoImage(file='img/logo_python.gif')

        # Depois criamos o título
        self.title = Label(self.window_frame)
        self.title.image = logo
        self.title['image'] = logo
        self.title.grid(row=1, column=1, columnspan=2)

        self.login_fields()

        # Então criamos o checkbutton para lembrar a senha e usuario
        self.checkbutton = Checkbutton(
            self.window_frame,
            font=self.font,
            text='Lembrar-me',
            background=BLUE,
            command=self.remember
        )
        self.checkbutton.grid(row=5, column=1, columnspan=2)
        self.selected = False

        # Criamos o botão de entrar/login
        login_image_button = PhotoImage(file='img/button_login.ppm')
        self.login_button = Button(
            self.button_frame,
            text='Login',
            command=self.login
        )
        self.login_button['image'] = login_image_button
        self.login_button.image = login_image_button
        self.login_button.grid(row=6, column=1)

        # E o botão para ir ao formulario de novo usuário
        self.new_user_button = Button(
            self.button_frame,
            text="Novo",
            command=self.new_user
        )
        self.new_user_button['image'] = self.button_image_new
        self.new_user_button.grid(row=6, column=2)

    def package_main_screen(self):
        """
        Empacota os elementos da tela principal
        """

        self.window_frame.pack()
        self.button_frame.pack()

    def login_fields(self):
        """
        Cria os campos de usuário e senha
        """

        # Depois criamos o label do usuário
        self.user_label = Label(
            self.window_frame,
            text="Usuário: ",
            font=self.font,
            background=BLUE
        )
        self.user_label.grid(row=2, column=1, sticky=EAST)

        # Colocamos o input do campo usuário
        self.user_input = Entry(
            self.window_frame,
            font=self.font,
            width=15
        )
        self.user_input.grid(row=2, column=2, sticky=WEST)

        # Colocamos a label da senha
        self.password_label = Label(
            self.window_frame,
            text="Senha: ",
            font=self.font,
            background=BLUE
        )
        self.password_label.grid(row=3, column=1, sticky=EAST)

        # E o campo da senha
        self.password_input = Entry(
            self.window_frame,
            show='*',
            font=self.font,
            width=15
        )
        self.password_input.grid(row=3, column=2, sticky=EAST)

        # E a label que vai devolver uma mensagem para o usuário
        self.message_label = Label(self.window_frame, text="")
        self.message_label.grid(row=4, column=1, columnspan=2)

    def destroy_main_screen(self):
        """
        Apaga os elementos da tela principal
        """

        self.window_frame.destroy()
        self.button_frame.destroy()
        self.title.destroy()
        self.user_label.destroy()
        self.user_input.destroy()
        self.password_label.destroy()
        self.password_input.destroy()
        self.checkbutton.destroy()
        self.message_label.destroy()
        self.login_button.destroy()
        self.new_user_button.destroy()

    def unpack_main_screen(self):
        """
        Esconde da tela todos os elementos da tela principal
        """

        self.button_frame.pack_forget()
        self.title.pack_forget()
        self.user_label.pack_forget()
        self.user_input.pack_forget()
        self.password_label.pack_forget()
        self.password_input.pack_forget()
        self.checkbutton.pack_forget()
        self.message_label.pack_forget()
        self.login_button.pack_forget()
        self.new_user_button.pack_forget()

    def fill_text_input(self):
        """
        Preenche o campo de texto com os dados de usuário e senha
        vindos do banco de dados
        """

        if 'Remember' in self.database:
            self.user_input.insert(0, self.database['Remember']['User'])
            self.password_input.insert(0, self.database['Remember']['Password'])

    def message(self, message, cor='red'):
        self.message_label["text"] = message
        self.message_label["foreground"] = cor

    def remember(self):
        """
        Função que troca o estado da variável do checkbutton
        """

        self.selected = not self.selected

    def login(self):
        """
        Função lida com a tentativa do usuário
        de tentar logar verificando se o usuário
        se encontra no database e se sua senha está
        correta e devolve uma mensagem adequada
        """

        user = self.user_input.get()
        password = self.password_input.get()

        if user not in self.database:
            self.message("Usuário Inválido")
        else:
            if password == self.database[user]['Password']:
                self.message("Bem vindo {0}".format(user), cor="blue")
                self.destroy_main_screen()
                self.application_screen()
                if self.selected:
                    self.database['Remember'] = {
                        'User': user,
                        'Password': password
                    }
            else:
                self.message("Senha Inválida")

    def new_user(self):
        """
        Faz as modificações necessárias para entrar no modo
        criar novo usuário e senha
        """

        self.unpack_main_screen()

        self.label_name = Label(
            self.window_frame,
            text='Nome',
            font=self.font,
            background=BLUE
        )
        self.input_name = Entry(self.window_frame, font=self.font)

        self.label_email = Label(
            self.window_frame,
            text='Email',
            font=self.font,
            background=BLUE
        )
        self.input_email = Entry(self.window_frame, font=self.font)

        self.button_create = Button(
            self.window_frame,
            image=self.button_image_create,
            command=self.register
        )

        self.packages_fields()

    def register(self):
        """
        Método usado para criar um novo usuário
        e uma senha
        """

        user = self.user_input.get()
        password = self.password_input.get()
        name = self.input_name.get()
        email = self.input_email.get()
        fields_are_empty = len(password) == 0 or \
                           len(user) == 0 or \
                           len(name) == 0 or \
                           len(email) == 0

        if fields_are_empty:
            self.message("Nenhum dos campos pode estar vazio!")
        elif user in self.database:
            self.message("Usuário já existe!")
        else:
            self.database[user] = {
                'Name': name,
                'Email': email,
                'Password': password
            }

            self.destroy_fields()

            self.user_input.delete(0, END)
            self.password_input.delete(0, END)

            self.package_main_screen()

            self.message('Usuário criado com sucesso', 'blue')

    def packages_fields(self):
        """
        Empacota todos os campos da tela de registro
        """

        # self.label_name.pack()
        # self.input_name.pack()
        # self.label_email.pack()
        # self.input_email.pack()
        self.user_label.pack()
        self.user_input.pack()
        self.password_label.pack()
        self.password_input.pack()
        self.button_create.pack()
        self.message_label.pack()

    def destroy_fields(self):
        """
        Destroi todos os campos da tela de registro
        """

        self.label_name.destroy()
        self.input_name.destroy()
        self.label_email.destroy()
        self.input_email.destroy()
        self.button_create.destroy()
        self.user_label.pack_forget()
        self.user_input.pack_forget()
        self.password_label.pack_forget()
        self.password_input.pack_forget()
        self.message_label.pack_forget()

    def application_screen(self):
        """
        Cria uma tela secundária para rodar os aplicativos
        """

        self.app_lines_button = Button(
            self.window,
            text='App Canvas 1 - Linhas',
            command=self.app_lines
        )

        self.app_spfc_button = Button(
            self.window,
            text='App Canvas 2 - SPFC',
            command=self.app_spfc
        )

        self.app_slices_button = Button(
            self.window,
            text='App Canvas 3 - Fatias',
            command=self.app_slices
        )

        self.app_face01_button = Button(
            self.window,
            text='App Canvas 4 - Carinha 1',
            command=self.app_face01
        )

        self.app_face02_button = Button(
            self.window,
            text='App Canvas 5 - Carinha 2',
            command=self.app_face02
        )

        self.app_mario_button = Button(
            self.window,
            text='App Canvas 6 - Mario',
            command=self.app_mario
        )

        self.app_draw_button = Button(
            self.window,
            text='App Canvas 7 - Desenha',
            command=self.app_draw
        )

        self.app_time_button = Button(
            self.window,
            text='App Canvas 8 - Horas',
            command=self.app_time
        )

        self.app_lines_button.pack(fill=BOTH, expand=True)
        self.app_spfc_button.pack(fill=BOTH, expand=True)
        self.app_slices_button.pack(fill=BOTH, expand=True)
        self.app_face01_button.pack(fill=BOTH, expand=True)
        self.app_face02_button.pack(fill=BOTH, expand=True)
        self.app_mario_button.pack(fill=BOTH, expand=True)
        self.app_draw_button.pack(fill=BOTH, expand=True)
        self.app_time_button.pack(fill=BOTH, expand=True)

    def app_lines(self):
        """
        Inicia o primeiro aplicativo com o canvas que é responsavel
        por desenhar algo utilizando linhas
        """

        self.destroy_application_screen()
        Lines(self.window)

    def app_spfc(self):
        """
        Inicia o segundo aplicativo com o canvas que é responsavel
        por desenha o brasão do São Paulo futebol clube
        """

        self.destroy_application_screen()
        SPFC(self.window)

    def app_slices(self):
        """
        Inicia o terceiro aplicativo com o canvas que é responsavel
        por desenha fatias/arcos dentro de um circulo
        """

        self.destroy_application_screen()
        Slices(self.window)

    def app_face01(self):
        """
        Inicio o quarto aplicativo com o canvas que é responsavel
        por desenhar um rostinho se movendo sozinho na tela e colidindo
        com as paredes
        """

        self.destroy_application_screen()
        Face01(self.window)

    def app_face02(self):
        """
        Inicia o quinto aplicativo com o canvas que é responsavel
        por desenhar um rostinho que será controlado pelas setas do
        teclado
        """

        self.destroy_application_screen()
        Face02(self.window)

    def app_mario(self):
        """
        Inicia o sexto aplicativo com o canvas que é responsavel
        por desenhar as sprints do mário e poder locomove-lo na tela
        """

        self.destroy_application_screen()
        Mario(self.window)

    def app_draw(self):
        """
        Inicia o setimo aplicativo com o canvas que é responsavel
        por desenhar na tela com cliques do mouse cada dois clique
        é uma linha de um ponto  a outro
        """

        self.destroy_application_screen()
        Draw(self.window)

    def app_time(self):
        """
        Inicia o oitavao aplicativo que é responsavel por mostrar
        as horas locais
        """

        self.destroy_application_screen()
        Time(self.window)

    def destroy_application_screen(self):
        """
        Destroi os elementos da tela de aplicação
        """

        self.app_lines_button.destroy()
        self.app_spfc_button.destroy()
        self.app_slices_button.destroy()
        self.app_face01_button.destroy()
        self.app_face02_button.destroy()
        self.app_mario_button.destroy()
        self.app_draw_button.destroy()
        self.app_time_button.destroy()


# Inicializamos a nossa janela
window = Tk()

# Inicializamos as variáveis do nosso programa
Login(window)

# Colocamos um titulo nela
window.title("Login")

# Definimos sua geometria
window.geometry = ("800x600")

window.resizable(False, False)
window.minsize(width=800, height=600)

# Definimos uma cor de fundo
window['background'] = BLUE

window.mainloop()

