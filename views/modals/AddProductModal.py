import customtkinter as ctk
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from tkinter import messagebox
import re

class AddProductModal:
    def __init__(self):
        # Window configuration
        self.app = ctk.CTk()
        self.app.title("Add Product")
        self.app.iconbitmap("assets/images/favicon.ico")
        gen.center_window(self.app, 400, 380)
        self.app.resizable(False, False)

        # Create frame for main content
        self.main_content = ctk.CTkFrame(master=self.app, width=400, height=380, corner_radius=0, fg_color="White")
        self.main_content.pack(fill="both", expand=True)

        # Create eimage

        # Create name label
        self.label_name = ctk.CTkLabel(master=self.main_content, text="Name", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_name.pack(pady=(20, 0), padx=10, anchor="w")

        # Create name input
        self.input_name = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                  corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the name of the user", 
                                  font=("Century Gothic", 12))
        self.input_name.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create description label
        self.label_username = ctk.CTkLabel(master=self.main_content, text="Description", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_username.pack(pady=0, padx=10, anchor="w")

        # Create description text area
        self.input_username = ctk.CTkTextbox(master=self.main_content, height=5, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                       corner_radius=10, text_color=PURPLE_MEDIUM, font=("Century Gothic", 12))
        self.input_username.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create price label
        self.label_email = ctk.CTkLabel(master=self.main_content, text="Price", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_email.pack(pady=0, padx=10, anchor="w")

        # Create price input
        self.input_email = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM,
                                    corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the price of the user",
                                    font=("Century Gothic", 12))
        self.input_email.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create stock label
        self.label_password = ctk.CTkLabel(master=self.main_content, text="Stock", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_password.pack(pady=0, padx=10, anchor="w")

        # Create stock input
        self.input_password = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM,
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the stock of the user",
                                      font=("Century Gothic", 12))
        self.input_password.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Crear botón para agregar usuario
        self.add_user_button = ctk.CTkButton(master=self.main_content, text="Add Product", font=("Century Gothic", 12), fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                             height=30, corner_radius=10, command=self.add_product)
        self.add_user_button.pack(pady=(10, 0), padx=10, anchor="w", fill="x")

        self.app.mainloop()

    async def add_product(self):
        try:
            # Get product data
            image = "https://firebasestorage.googleapis.com/v0/b/store-management-88a00.appspot.com/o/default%2Fno-image-product.jpeg?alt=media&token=ff9a65fe-7fab-4e4c-8418-715f71d9e2ef"
            name = self.input_name.get()
            description = self.input_username.get("1.0", "end-1c")
            price = self.input_email.get()
            stock = self.input_password.get()

            product_data = {
                "image": image,
                "name": name,
                "description": description,
                "price": price,
                "stock": stock
            }

            # Validate data
            if name == "" or description == "" or price == "" or stock == "":
                messagebox.showerror("Error", "All fields are required")
                return
            
            if not re.match(r"^\d+(?:\.\d{1,2})?$", price):
                messagebox.showerror("Error", "Invalid price format")
                return
            
            if not re.match(r"^\d+$", stock):
                messagebox.showerror("Error", "Invalid stock format")
                return
            
            # Add product to Firebase
            await fb.insert_collection(self, "products", product_data)
            messagebox.showinfo("Success", "Product added successfully")
            self.app.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.app.destroy()

