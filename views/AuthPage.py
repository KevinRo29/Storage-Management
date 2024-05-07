import customtkinter as ctk
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from views.MainPanel import MainPanel
from tkinter import messagebox

class AuthPage:
    def __init__(self):
        # Configuración de la ventana
        app = ctk.CTk()
        app.title("Login")
        app.iconbitmap("assets/images/favicon.ico")
        gen.center_window(app, 700, 400)
        app.resizable(False, False)

        # Crear frame para la imagen
        image_frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=0)
        image_frame.pack(side="left", fill="y")

        # Crear frame para el formulario
        form_frame = ctk.CTkFrame(master=app, width=400, height=400, corner_radius=0, fg_color="White")
        form_frame.pack(side="right", fill="both", expand=True)

        # Agregar imagen
        image = gen.read_image("assets/images/Login.jpeg", (300, 400))
        image_label = ctk.CTkLabel(master=image_frame, image=image, text="")
        image_label.pack(pady=(0, 0))

        # Crear formulario centrado
        form = ctk.CTkFrame(master=form_frame, width=400, height=400, corner_radius=0, fg_color="transparent")
        form.pack(expand=True)

        # Texto de bienvenida
        welcome_text = ctk.CTkLabel(master=form, text="WELCOME!", font=("Century Gothic", 25), text_color=PURPLE_MEDIUM, anchor="w")
        welcome_text.pack(pady=(10, 0), padx=10, anchor="w")

        # Texto de "Inicia sesion con tu cuenta"
        login_text = ctk.CTkLabel(master=form, text="Login with your account", font=("Century Gothic", 15), text_color=GRAY, anchor="w")
        login_text.pack(pady=(0, 0), padx=10, anchor="w")

        # Crear etiqueta e input de username
        label_username = ctk.CTkLabel(master=form, text="Username", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        label_username.pack(pady=(20, 0), padx=10, anchor="w")

        input_username = ctk.CTkEntry(master=form, width=300, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter your username", 
                                      font=("Century Gothic", 12))
        input_username.pack(pady=(0, 10), padx=10)

        # Crear etiqueta e input de password
        label_password = ctk.CTkLabel(master=form, text="Password", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        label_password.pack(pady=0, padx=10, anchor="w")

        input_password = ctk.CTkEntry(master=form, width=300, height=35, show="*", fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter your password", 
                                      font=("Century Gothic", 12))
        input_password.pack(pady=(0, 10), padx=10)

        # Crear botón de login
        button_login = ctk.CTkButton(master=form, text="Sign In", fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK, font=("Century Gothic", 12),
                                     command=lambda: sign_in(input_username.get(), input_password.get()), width=300, height=35)
        button_login.pack(pady=10, padx=10)

        # Función de login
        def sign_in(username, password):
            # Se agregla el disabled al botón para evitar que se haga click varias veces
            button_login.configure(state="disabled")

            # Verificar si el usuario y contraseña son correctos
            valid_user = fb.sign_in(self, username, password)

            # Si el usuario es válido, abrir la ventana principal
            if valid_user:
                app.destroy()
                MainPanel()
                button_login.configure(state="normal")

            # Si el usuario no es válido, mostrar un mensaje de error
            else:
                messagebox.showerror("Error", "Invalid username or password")
                button_login.configure(state="normal")

        # Iniciar la aplicación
        app.mainloop()
