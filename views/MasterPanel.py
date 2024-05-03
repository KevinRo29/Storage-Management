import tkinter as tk
from tkinter import font
from config import COLOR_NAVBAR, COLOR_SIDE_BAR, COLOR_BODY, COLOR_MENU_HOVER
from utils import generic as gen

class MasterPanel(tk.Tk):
    def __init__(self):
        # Initializes the parent class
        super().__init__()

        # Load the images
        self.logo = gen.read_image("assets/images/Logo.jpeg", (100, 100))
        self.profile = gen.read_image("assets/images/photo-profile.jpeg", (150, 150))

        # Config the window
        self.config_window()

        # Load the panels
        self.panels()

        # Load the top bar controls
        self.top_bar_controls()

        # Load the side bar controls
        self.side_bar_controls()

    def config_window(self):
        # Config the window
        self.title("Master Panel")

        # Change the window icon
        self.iconbitmap("assets/images/favicon.ico")

        # Change the window size
        gen.center_window(self, 800, 600)

    def panels(self):
        # Navbar
        self.navbar = tk.Frame(self, bg=COLOR_NAVBAR, height=50)
        self.navbar.pack(side="top", fill="both")

        # Sidebar
        self.side_bar = tk.Frame(self, bg=COLOR_SIDE_BAR, width=200)
        self.side_bar.pack(side="left", fill="both", expand=False)

        # Body
        self.body = tk.Frame(self, bg=COLOR_BODY)
        self.body.pack(side="right", fill="both", expand=True)

    def top_bar_controls(self):
        # Config the top bar
        font_awesome = font.Font(family="FontAwesome", size=12)

        # Title label
        self.title_label = tk.Label(self.navbar, text="Master Panel")
        self.title_label.config(fg="white", font=("Roboto", 15), bg=COLOR_NAVBAR, pady=10, width=17)
        self.title_label.pack(side="left")

        # Sidebar toggle button
        self.sidebar_toggle = tk.Button(self.navbar, text="\u2630", font=font_awesome, bg=COLOR_NAVBAR, fg="white", bd=0)
        self.sidebar_toggle.pack(side="left")

        # Informaton label
        self.info_label = tk.Label(self.navbar, text="Welcome, User")
        self.info_label.config(fg="white", font=("Roboto", 12), bg=COLOR_NAVBAR, pady=10, width=20)
        self.info_label.pack(side="right")
        
    def side_bar_controls(self):
        width_menu = 20
        height_menu = 2
        font_awesome = font.Font(family="FontAwesome", size=15)

        # Profile Label
        self.profile_label = tk.Label(self.side_bar, image=self.profile, bg=COLOR_SIDE_BAR)
        self.profile_label.pack(side="top", pady=10)

        #Buttons to navigate
        self.homeButton = tk.Button(self.side_bar)
        self.productsButton = tk.Button(self.side_bar)
        self.customersButton = tk.Button(self.side_bar)
        self.settingsButton = tk.Button(self.side_bar)
        self.logoutButton = tk.Button(self.side_bar)

        menu_buttons = [
            ("Home", "\U0001F3E0", self.homeButton),
            ("Products","\U0001F4E6", self.productsButton),
            ("Customers","\U0001F465", self.customersButton),
            ("Settings","\U00002699", self.settingsButton),
            ("Logout","\U0001F6AA", self.logoutButton)
        ]

        for text, icon, button in menu_buttons:
            self.button_menu_config(button, text, icon, font_awesome, width_menu, height_menu)

    def button_menu_config(self, button, text, icon, font_awesome, width, height):
        button.config(text=f"{icon} {text}", anchor='w', font=font_awesome, bg=COLOR_SIDE_BAR, fg="white", bd=0, width=width, height=2)
        button.pack(side="top", pady=3, padx=10, fill="both")
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_HOVER, fg="black")

    def on_leave(self, event, button):
        button.config(bg=COLOR_SIDE_BAR, fg="white")