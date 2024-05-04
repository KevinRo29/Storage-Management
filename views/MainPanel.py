import customtkinter as ctk
from utils import generic as gen
from config import *
from views import ProductsPage, ProfilePage, AdminPage, HomePage, AuthPage

class MainPanel:
    def __init__(self):
        # Configuración de la ventana
        app = ctk.CTk()
        app.title("Main Panel")
        app.iconbitmap("assets/images/favicon.ico")
        gen.center_window(app, 1100, 650)
        app.minsize(800, 650)
        app.resizable(True, True)

        # Crear frame para el menu lateral
        self.side_menu = ctk.CTkFrame(master=app, width=200, height=650, corner_radius=0, fg_color=PURPLE_MEDIUM)
        self.side_menu.pack(side="left", fill="y")

        # Crear frame para el contenido principal y usar HomePage
        self.main_content = ctk.CTkFrame(master=app, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)
        HomePage.HomePage(self.main_content)

        # Crear nombre de usuario
        self.username_label = ctk.CTkLabel(master=self.side_menu, text="Username", font=("Century Gothic", 15), text_color="White")
        self.username_label.pack(pady=(20, 5))

        # Crear imagen de perfil
        self.profile_image = gen.read_image("assets/images/photo-profile.jpeg", (100, 100))
        self.profile_image_label = ctk.CTkLabel(master=self.side_menu, image=self.profile_image, text="")
        self.profile_image_label.pack(pady=(5, 20))

        # Crear texto: Dashboard
        self.dashboard_text = ctk.CTkLabel(master=self.side_menu, text="MENU", font=("Century Gothic", 15), text_color="White")
        self.dashboard_text.pack(pady=(10, 10))

        # Variable con los  botones del menú y las propiedas: icon, text, command
        menu_buttons = [
            {"icon": "assets/icons/home.png", "text": "Home", "command": self.show_home_page},
            {"icon": "assets/icons/products.png", "text": "Products", "command": self.show_products_page},
            {"icon": "assets/icons/admin.png", "text": "Admin", "command": self.show_admin_page},
            {"icon": "assets/icons/profile.png", "text": "Profile", "command": self.show_profile_page},
            {"icon": "assets/icons/logout.png", "text": "Logout", "command": app.destroy}
        ]

        # Crear botones del menú
        for button in menu_buttons:
            if button["icon"] == "assets/icons/logout.png":
                button_image = gen.read_image(button["icon"], (13, 13))
                button_label = ctk.CTkButton(master=self.side_menu, image=button_image, text=button["text"], font=("Century Gothic", 12), 
                                            fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK, width=200, height=30, command=button["command"])
                button_label.pack(pady=(0, 20), padx=15, anchor="w", side="bottom")
            else:
                button_image = gen.read_image(button["icon"], (20, 20))
                button_label = ctk.CTkButton(master=self.side_menu, image=button_image, text=button["text"], font=("Century Gothic", 12), 
                                            fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK, width=200, height=30, command=button["command"], anchor="w")
                button_label.pack(pady=7, padx=15, anchor="w")

        app.mainloop()

    def clear_content(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def show_home_page(self):
        self.clear_content()
        HomePage.HomePage(self.main_content)

    def show_admin_page(self):
        self.clear_content()
        AdminPage.AdminPage(self.main_content)

    def show_products_page(self):
        self.clear_content()
        ProductsPage.ProductsPage(self.main_content)

    def show_profile_page(self):
        self.clear_content()
        ProfilePage.ProfilePage(self.main_content)
