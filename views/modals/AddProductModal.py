import customtkinter as ctk
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from tkinter import messagebox
import re

class AddProductModal:
    def __init__(self, products_page_instance):
        self.products_page_instance = products_page_instance
        # Window configuration
        self.app = ctk.CTk()
        self.app.title("Add Product")
        self.app.iconbitmap("assets/images/favicon.ico")
        gen.center_window(self.app, 400, 380)
        self.app.resizable(False, False)

        # Create frame for main content
        self.main_content = ctk.CTkScrollableFrame(master=self.app, width=400, height=380, corner_radius=0, fg_color="White")
        self.main_content.pack(fill="both", expand=True)

        # Create name label
        self.label_name = ctk.CTkLabel(master=self.main_content, text="Name", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_name.pack(pady=(10, 0), padx=10, anchor="w")

        # Create name input
        self.input_name = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, 
                                  corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the name of the product", 
                                  font=("Century Gothic", 12))
        self.input_name.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create description label
        self.label_description = ctk.CTkLabel(master=self.main_content, text="Description", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_description.pack(pady=0, padx=10, anchor="w")

        # Create description text area
        self.textbox_description = ctk.CTkTextbox(master=self.main_content, height=5, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, border_width=2,
                                       corner_radius=10, text_color=PURPLE_MEDIUM, font=("Century Gothic", 12))
        self.textbox_description.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create price label
        self.label_price = ctk.CTkLabel(master=self.main_content, text="Price", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_price.pack(pady=0, padx=10, anchor="w")

        # Create price input
        self.input_price = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM,
                                    corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the price of the product",
                                    font=("Century Gothic", 12))
        self.input_price.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Create stock label
        self.label_stock = ctk.CTkLabel(master=self.main_content, text="Stock", text_color=PURPLE_MEDIUM, font=("Century Gothic", 12), anchor="w")
        self.label_stock.pack(pady=0, padx=10, anchor="w")

        # Create stock input
        self.input_stock = ctk.CTkEntry(master=self.main_content, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM,
                                      corner_radius=10, text_color=PURPLE_MEDIUM, placeholder_text="Enter the stock of the product",
                                      font=("Century Gothic", 12))
        self.input_stock.pack(pady=(0, 10), padx=10, anchor="w", fill="x")

        # Crear botón para agregar usuario
        self.add_product_button = ctk.CTkButton(master=self.main_content, text="Add Product", font=("Century Gothic", 12), fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                             height=30, corner_radius=10, command=self.add_product)
        self.add_product_button.pack(pady=(10, 0), padx=10, anchor="w", fill="x")

        self.app.mainloop()

    def add_product(self):
        try:
            # Get product data
            image = "https://firebasestorage.googleapis.com/v0/b/store-management-88a00.appspot.com/o/default%2Fno-image-product.jpeg?alt=media&token=ff9a65fe-7fab-4e4c-8418-715f71d9e2ef"
            name = self.input_name.get()
            description = self.textbox_description.get("1.0", "end-1c")
            price = self.input_price.get()
            stock = self.input_stock.get()

            product_data = {
                "image": image,
                "name": name,
                "description": description,
                "price": price,
                "stock": stock,
                "status": "active"
            }

            # Validate data
            if name == "" or description == "" or price == "" or stock == "":
                messagebox.showerror("Error", "All fields are required", parent=self.app)
                return
            
            if not re.match(r"^\d+(?:\.\d{1,2})?$", price):
                messagebox.showerror("Error", "Invalid price format", parent=self.app)
                return
            
            if not re.match(r"^\d+$", stock):
                messagebox.showerror("Error", "Invalid stock format", parent=self.app)
                return
            
            # Add product to Firebase
            fb.insert_collection(self, "products", product_data)

            messagebox.showinfo("Success", "Product added successfully", parent=self.app)

            # Refresh products table
            self.products_page_instance.refresh_products()

            self.app.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.app)
            self.app.destroy()

