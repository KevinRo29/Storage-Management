import customtkinter as ctk
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from views.modals.AddProductModal import AddProductModal
from views.modals.EditProductModal import EditProductModal
from tkinter import filedialog, messagebox

products_data = [
]

class ProductsPage:
    def __init__(self, parent_frame):
        products_data.clear()
        
        self.get_products_data()

        # Create a frame for the main content
        self.main_content = ctk.CTkFrame(master=parent_frame, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Create a frame for the header section
        self.users_frame = ctk.CTkFrame(master=self.main_content, width=900, height=75, corner_radius=0, fg_color="White")
        self.users_frame.pack(side="top", fill="x")

        # Label for "Products" on the left side
        self.users_label = ctk.CTkLabel(master=self.users_frame, text="PRODUCTS", font=("Century Gothic", 20), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.users_label.pack(side="left", padx=(20, 0), pady=0, fill="y")

        # Button for "Add User" with an icon on the right side
        self.add_user_icon = gen.read_image("assets/icons/add-product.png", (15, 15))
        self.add_user_button = ctk.CTkButton(master=self.users_frame, text="Add Product", image=self.add_user_icon, fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                        height=25, command=self.show_add_user_modal)
        self.add_user_button.pack(side="right", padx=(0, 20), pady=22)

        # Frame for the search field
        self.search_frame = ctk.CTkFrame(master=self.main_content, width=900, height=50, corner_radius=0, fg_color="White")
        self.search_frame.pack(side="top", fill="x")

        # Refresh button on the right side
        self.refresh_icon = gen.read_image("assets/icons/refresh.png", (15, 15))
        self.refresh_button = ctk.CTkButton(master=self.search_frame, image=self.refresh_icon, fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                      text="Refresh", height=25, width=50, command=self.refresh_products)
        self.refresh_button.pack(side="right", padx=(0, 20), pady=10)

        # The remaining space is for the frame where the table of all users will be located
        self.users_table_frame = ctk.CTkScrollableFrame(master=self.main_content, width=900, height=525, corner_radius=0, fg_color="White")
        self.users_table_frame.pack(side="top", fill="both", expand=True)

        # Create the table of users
        self.create_products_card()

    def show_add_user_modal(self):
        AddProductModal(self)

    def refresh_products(self):
        # Clear the current products data
        products_data.clear()

        # Get the updated products data
        self.get_products_data()

        # Destroy the current products table
        for widget in self.users_table_frame.winfo_children():
            widget.destroy()

        # Create the updated products table
        self.create_products_card()

    def create_products_card(self):
        products_per_row = 3
        num_products = len(products_data)
        available_width = self.users_table_frame.winfo_width()  # Obtiene el ancho disponible del frame contenedor

        # Calcula el ancho de cada tarjeta de producto basado en el número de productos por fila
        card_width = available_width / products_per_row

        # Iterate over products, organizing them into rows
        for i in range(0, num_products, products_per_row):
            # Create a frame for each row
            row_frame = ctk.CTkFrame(master=self.users_table_frame, width=available_width, height=200, corner_radius=0, fg_color="White")
            row_frame.pack(side="top", fill="x")

            # Iterate over products in the current row
            for product in products_data[i:i+products_per_row]:
                product_card = ctk.CTkFrame(master=row_frame, width=card_width, height=200, corner_radius=12, fg_color="gray")
                product_card.pack(side="left", padx=10, pady=10, expand=True)  # Ajusta al ancho disponible

                product_image = gen.read_image_from_url(product[1], (200, 200))
                product_image_label = ctk.CTkLabel(master=product_card, image=product_image, fg_color="transparent", 
                                                   text="")
                product_image_label.pack(side="top", padx=10, pady=10, fill="x")
                product_image_label.bind("<Button-1>", lambda event, product_id=product[0]: self.updated_product_image(product_id))
                product_image_label.configure(cursor="hand2")

                product_name = ctk.CTkLabel(master=product_card, text=product[2], font=("Century Gothic", 14), fg_color="transparent", text_color="White")
                product_name.pack(side="top", padx=10, pady=2, fill="x")

                product_description = ctk.CTkLabel(master=product_card, text=product[3], font=("Century Gothic", 12), fg_color="transparent", text_color="White")
                product_description.pack(side="top", padx=10, pady=2, fill="x")

                product_price = ctk.CTkLabel(master=product_card, text="$" + str(product[4]), font=("Century Gothic", 12), fg_color="transparent", text_color="White")
                product_price.pack(side="top", padx=10, pady=2, fill="x")

                product_stock = ctk.CTkLabel(master=product_card, text="Stock: " + str(product[5]), font=("Century Gothic", 12), fg_color="transparent", text_color="White")
                product_stock.pack(side="top", padx=10, pady=2, fill="x")

                # Edit button with full width
                edit_icon = gen.read_image("assets/icons/edit.png", (15, 15))
                edit_button = ctk.CTkButton(master=product_card, text="Edit Product", image=edit_icon, fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                             height=25, width=50, command=lambda product=product: self.show_edit_product_modal(product))
                edit_button.pack(side="bottom", padx=10, pady=10, fill="x")

    def get_products_data(self):
        products = fb.get_active_collection(self, "products")
        for product in products:
            products_data.append([product["id"], product["image"], product["name"], product["description"], product["price"], product["stock"]])

    def updated_product_image(self, product_id):
        try:
            # Open a dialog to select a file
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png")])
            if file_path:
                # Folder name
                folder_name = "ProductsPictures"

                # Set the name of the file
                file_name = "Product_Image_" + product_id

                # Upload the image to Firebase Storage
                url_image = fb.upload_image(self, file_path, file_name, folder_name)

                # Update the product's image
                for product in products_data:
                    if product[0] == product_id:
                        product[1] = url_image

                # Destroy the current products table
                for widget in self.users_table_frame.winfo_children():
                    widget.destroy()

                # Create the updated products table
                self.create_products_card()

                # Update the product's image in the database
                fb.update_collection(self, "products", product_id, {"image": url_image})

                # Show success message
                messagebox.showinfo("Success", "Product image updated successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    def show_edit_product_modal(self, product):
        EditProductModal(self, product)