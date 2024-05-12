import customtkinter as ctk
from utils import generic as gen
from config import *

class HomePage:
    def __init__(self, parent_frame):
        self.main_content = ctk.CTkFrame(master=parent_frame, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Create a text "Welcome to the Home Page"
        welcome_label = ctk.CTkLabel(master=self.main_content, text="Welcome to the Home Page", font=("Century Gothic", 20), fg_color="transparent", text_color=PURPLE_MEDIUM)
        welcome_label.pack(side="top", padx=20, pady=20, fill="y")
        