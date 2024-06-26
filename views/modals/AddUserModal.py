import customtkinter as ctk
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from tkinter import messagebox
import re

class AddUserModal:
    def __init__(self):
        # Window configuration
        self.app = ctk.CTk()
        self.app.title("Add User")
        self.app.iconbitmap("assets/images/favicon.ico")
        gen.center_window(self.app, 400, 380)
        self.app.resizable(False, False)

        # Create frame for main content
        self.main_content = ctk.CTkFrame(master=self.app, width=400, height=380, corner_radius=0, fg_color="White")
        self.main_content.pack(fill="both", expand=True)

        # Create name label
        self.label_name = ctk.CTkLabel(master=self.main_content, text="Name", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_name.pack(pady=(20, 0), padx=10, anchor="w")

        # Create name input
        self.input_name = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                  corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the name of the user", 
                                  font=("Century Gothic", 12))
        self.input_name.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create email label
        self.label_email = ctk.CTkLabel(master=self.main_content, text="Email", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_email.pack(pady=0, padx=10, anchor="w")

        # Create email input
        self.input_email = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                  corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the email of the user", 
                                  font=("Century Gothic", 12))
        self.input_email.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create username label
        self.label_username = ctk.CTkLabel(master=self.main_content, text="Username", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_username.pack(pady=0, padx=10, anchor="w")

        # Create username input
        self.input_username = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the username of the user", 
                                      font=("Century Gothic", 12))
        self.input_username.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create password label
        self.label_password = ctk.CTkLabel(master=self.main_content, text="Password", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_password.pack(pady=0, padx=10, anchor="w")

        # Create password input
        self.input_password = ctk.CTkEntry(master=self.main_content, height=35, show="*", fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the password of the user", 
                                      font=("Century Gothic", 12))
        self.input_password.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Crear botón para agregar usuario
        self.add_user_button = ctk.CTkButton(master=self.main_content, text="Add User", font=("Century Gothic", 12), fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                             height=30, corner_radius=10, command=self.add_user)
        self.add_user_button.pack(pady=(10, 0), padx=10, anchor="w", fill="x")

        self.app.mainloop()

    async def add_user(self):
        # Get user data
        name = self.input_name.get()
        lastname = ""
        email = self.input_email.get()
        username = self.input_username.get()
        password = self.input_password.get()
        phone = ""
        profile_image = "https://firebasestorage.googleapis.com/v0/b/store-management-88a00.appspot.com/o/default%2Fdefault_image.png?alt=media&token=fdc5296f-2a8d-406a-9e3f-fbc414270c94"
        role = "worker"

        #Call the function to validate the email
        email_valid = self.validate_email(email)

        if not email_valid:
            messagebox.showerror("Error", "Invalid email", parent=self.app)
            return
        
        # Check if all inputs are filled
        if name and email and username and password:
            user_exists = fb.verify_user(self, username, email)

            if user_exists:
                messagebox.showerror("Error", "Username or email already exists", parent=self.app)
                return
            
            # Encript password
            password = gen.encrypt_password(password)

            # Create user data
            user_data = {
                "name": name,
                "lastname": lastname,
                "email": email,
                "username": username,
                "password": password,
                "phone": phone,
                "profile_image": profile_image,
                "role": role,
                "status": "active"
            }

            # Insert user data in collection
            fb.insert_collection(self, "users", user_data)

            # Close modal
            self.app.destroy()

            # Show success message
            await messagebox.showinfo("Success", "User added successfully", parent=self.app)
        else:
            messagebox.showerror("Error", "All fields are required", parent=self.app)

    def validate_email(self, email):
        regex = r"[^@]+@[^@]+\.[^@]+"

        if re.match(regex, email):
            return True
        else:
            return False
