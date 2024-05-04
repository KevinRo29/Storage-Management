import customtkinter as ctk
from utils import generic as gen
from config import *

class ProfilePage:
    def __init__(self, parent_frame):
        self.main_content = ctk.CTkFrame(master=parent_frame, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)
        self.profile_label = ctk.CTkLabel(master=self.main_content, text="Profile Page", font=("Century Gothic", 20), text_color="Black")
        self.profile_label.pack(pady=(20, 20))
        self.profile_text = ctk.CTkLabel(master=self.main_content, text="Welcome to the Profile Page", font=("Century Gothic", 15), text_color="Black")
        self.profile_text.pack(pady=(0, 20))