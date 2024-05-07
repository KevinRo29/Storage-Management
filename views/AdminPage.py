import customtkinter as ctk
from CTkTable import *
from utils import generic as gen
from config import *
from services.firebase import FirebaseService as fb
from views.modals.AddUserModal import AddUserModal

users_data_table = [
    ["Name", "Lastname", "Username", "Email", "Phone"],
]

class AdminPage:
    def __init__(self, parent_frame):

        #Call the funcion to get the user data
        self.get_users_data()

        # Create a frame for the main content
        self.main_content = ctk.CTkFrame(master=parent_frame, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Create a frame for the header section
        self.users_frame = ctk.CTkFrame(master=self.main_content, width=900, height=75, corner_radius=0, fg_color="White")
        self.users_frame.pack(side="top", fill="x")

        # Label for "Users" on the left side
        users_label = ctk.CTkLabel(master=self.users_frame, text="USERS", font=("Century Gothic", 20), fg_color="transparent", text_color=PURPLE_MEDIUM)
        users_label.pack(side="left", padx=(20, 0), pady=0, fill="y")

        # Button for "Add User" with an icon on the right side
        add_user_icon = gen.read_image("assets/icons/add-user.png", (15, 15))
        add_user_button = ctk.CTkButton(master=self.users_frame, text="Add User", image=add_user_icon, fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                        height=25, command=self.show_add_user_modal)
        add_user_button.pack(side="right", padx=(0, 20), pady=22)

        # Frame for the search field
        self.search_frame = ctk.CTkFrame(master=self.main_content, width=900, height=50, corner_radius=0, fg_color="White")
        self.search_frame.pack(side="top", fill="x")

        # Search field
        self.search_field = ctk.CTkEntry(master=self.search_frame, width=600, fg_color="White", corner_radius=10, 
                                         border_width=2, text_color=PURPLE_MEDIUM, border_color=PURPLE_MEDIUM, placeholder_text="Search user by keyword")
        self.search_field.pack(side="left", padx=(20, 0), pady=10)

        # Refresh button on the right side
        refresh_icon = gen.read_image("assets/icons/refresh.png", (15, 15))
        refresh_button = ctk.CTkButton(master=self.search_frame, image=refresh_icon, fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK,
                                      text="Refresh", height=25, width=50, command=self.refresh_users_table)
        refresh_button.pack(side="right", padx=(0, 20), pady=10)

        # The remaining space is for the frame where the table of all users will be located
        self.users_table_frame = ctk.CTkScrollableFrame(master=self.main_content, width=900, height=525, corner_radius=0, fg_color="White")
        self.users_table_frame.pack(side="top", fill="both", expand=True)

        # Create the table of users
        self.create_users_table()

    def create_users_table(self):
        # Crea la tabla con los encabezados
        self.users_table = CTkTable(master=self.users_table_frame, values=users_data_table, colors=["#E6E6E6", "#EEEEEE"], 
                                    header_color=PURPLE_MEDIUM, text_color="Black", corner_radius=5)
        self.users_table.edit_row(0, text_color="White")
        self.users_table.pack(expand=True, fill="both", padx=20, pady=(10, 20))

        # Vincula el evento de tecla presionada en el campo de búsqueda con el método de filtrado
        self.search_field.bind("<KeyRelease>", self.filter_users_table)

    def show_add_user_modal(self):
        # Create the modal to add a new user
        AddUserModal()

    def refresh_users_table(self):
        # Limpia la tabla y los datos de usuario
        self.users_table.destroy()
        users_data_table.clear()
        users_data_table.append(["Name", "Lastname", "Username", "Email", "Phone"])
        self.get_users_data()

        # Recrea la tabla con los datos actualizados
        self.create_users_table()

    def get_users_data(self):
        # Get all users from the database
        users = fb.get_active_collection(self, "users")

        #Add the information to users_data
        for user in users:
            users_data_table.append([user["name"], user["lastname"], user["username"], user["email"], user["phone"], "Edit"])
    
    def filter_users_table(self, event=None):
        # Obtiene la palabra clave de búsqueda del campo de búsqueda
        keyword = self.search_field.get().lower()

        # Filtra los datos de usuario según la palabra clave
        filtered_users = [user for user in users_data_table[1:] if any(keyword in str(field).lower() for field in user)]

        # Actualiza la tabla con los usuarios filtrados
        self.users_table.update_values([users_data_table[0]] + filtered_users)
