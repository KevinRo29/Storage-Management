import customtkinter as ctk
from utils import generic as gen
from config import *
from services import global_vars as gv
from services.firebase import FirebaseService as fb
from tkinter import filedialog, messagebox

class ProfilePage:
    def __init__(self, parent_frame, main_panel_instance):
        self.main_panel = main_panel_instance

        self.main_content = ctk.CTkFrame(master=parent_frame, width=900, height=650, corner_radius=0, fg_color="White")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Create a frame for the header section
        self.users_frame = ctk.CTkFrame(master=self.main_content, width=900, height=75, corner_radius=0, fg_color="White")
        self.users_frame.pack(side="top", fill="x")

        # Create a frame for the body section
        self.body_frame = ctk.CTkFrame(master=self.main_content, width=900, height=575, corner_radius=0, fg_color="White")
        self.body_frame.pack(side="top", fill="both", expand=True)

        # On the right side, create a frame for the user's profile picture
        self.profile_frame = ctk.CTkFrame(master=self.users_frame, width=75, height=10)
        self.profile_frame.pack(side="right", padx=(0, 20), pady=20)

        # Label for "Profile" on the left side
        self.users_label = ctk.CTkLabel(master=self.users_frame, text="PROFILE", font=("Century Gothic", 20), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.users_label.pack(side="left", padx=(20, 0), pady=20, fill="y")

        # Load photo from the user's profile picture
        self.profile_picture = gen.read_image_from_url(gv.user_data["profile_image"], (75, 75))
        self.profile_label = ctk.CTkLabel(master=self.profile_frame, image=self.profile_picture, text="")
        self.profile_label.pack(side="top")
        
        # Add a button to change profile picture
        self.change_picture_button = ctk.CTkButton(master=self.profile_frame, text="Change", font=("Century Gothic", 10), width=75, height=25,
                                                   fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK, command=self.change_profile_picture)
        self.change_picture_button.pack(side="bottom")

        # Create a frame for the user's information
        self.info_frame = ctk.CTkFrame(master=self.body_frame, width=900, height=575, corner_radius=0, fg_color="White")
        self.info_frame.pack(side="top", fill="both", expand=True)

        # Create a label for the user's name
        self.name_label = ctk.CTkLabel(master=self.info_frame, text="Name", font=("Century Gothic", 14), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.name_label.pack(side="top", padx=20, pady=(20, 0), anchor="w")

        # Create an entry for the user's name
        self.name_entry = ctk.CTkEntry(master=self.info_frame, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, corner_radius=10, text_color=PURPLE_MEDIUM,
                                        placeholder_text="Enter your name", font=("Century Gothic", 14))
        self.name_entry.insert(0, gv.user_data["name"])
        self.name_entry.pack(side="top", padx=20, pady=(0, 10), fill="x")

        # Create a label for the user's last name
        self.last_name_label = ctk.CTkLabel(master=self.info_frame, text="Last Name", font=("Century Gothic", 14), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.last_name_label.pack(side="top", padx=20, anchor="w")

        # Create an entry for the user's last name
        self.last_name_entry = ctk.CTkEntry(master=self.info_frame, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, corner_radius=10, text_color=PURPLE_MEDIUM,
                                            placeholder_text="Enter your last name", font=("Century Gothic", 14))
        self.last_name_entry.insert(0, gv.user_data["lastname"])
        self.last_name_entry.pack(side="top", padx=20, pady=(0, 10), fill="x")

        # Create a label for the user's email
        self.email_label = ctk.CTkLabel(master=self.info_frame, text="Email", font=("Century Gothic", 14), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.email_label.pack(side="top", padx=20, anchor="w")

        # Create an entry for the user's email
        self.email_entry = ctk.CTkEntry(master=self.info_frame, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, corner_radius=10, text_color=PURPLE_MEDIUM,
                                         placeholder_text="Enter your email", font=("Century Gothic", 14))
        self.email_entry.insert(0, gv.user_data["email"])
        self.email_entry.pack(side="top", padx=20, pady=(0, 10), fill="x")

        # Create a label for the user's username
        self.username_label = ctk.CTkLabel(master=self.info_frame, text="Username", font=("Century Gothic", 14), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.username_label.pack(side="top", padx=20, anchor="w")

        # Create an entry for the user's username
        self.username_entry = ctk.CTkEntry(master=self.info_frame, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, corner_radius=10, text_color=PURPLE_MEDIUM,
                                           placeholder_text="Enter your username", font=("Century Gothic", 14))
        self.username_entry.insert(0, gv.user_data["username"])
        self.username_entry.pack(side="top", padx=20, pady=(0, 10), fill="x")

        # Create a label for the user's phone number
        self.phone_label = ctk.CTkLabel(master=self.info_frame, text="Phone", font=("Century Gothic", 14), fg_color="transparent", text_color=PURPLE_MEDIUM)
        self.phone_label.pack(side="top", padx=20, anchor="w")

        # Create an entry for the user's phone number
        self.phone_entry = ctk.CTkEntry(master=self.info_frame, height=35, fg_color=PURPLE_WHITE, border_color=PURPLE_MEDIUM, corner_radius=10, text_color=PURPLE_MEDIUM,
                                         placeholder_text="Enter your phone number", font=("Century Gothic", 14))
        self.phone_entry.insert(0, gv.user_data["phone"])
        self.phone_entry.pack(side="top", padx=20, pady=(0, 10), fill="x")

        # Add button to save information but in a hidden state
        self.save_button = ctk.CTkButton(master=self.info_frame, text="Update Profile", font=("Century Gothic", 12), width=150, height=35,
                                         fg_color=PURPLE_MEDIUM, hover_color=PURPLE_DARK, command=self.save_information)
        self.save_button.pack(side="top", padx=(0, 20), pady=20)
        
    def change_profile_picture(self):
        try:
            # Open a dialog to select a file
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png")])
            if file_path:
                # Set the name of the file
                file_name = "Profile_Picture_" + gv.user_data["id"]

                # Upload the image to Firebase Storage
                url_image = fb.upload_image(self, file_path, file_name)

                # Update the user's profile picture
                gv.user_data["profile_image"] = url_image
                self.profile_picture = gen.read_image_from_url(url_image, (75, 75))
                self.profile_label.configure(image=self.profile_picture)

                # Update the user's profile picture in the database
                fb.update_collection(self, "users", gv.user_data["id"], {"profile_image": url_image})

                # Update the user's profile picture in the global variables
                gv.user_data["profile_image"] = url_image

                self.main_panel.update_profile_image(url_image)

                # Show a success message
                messagebox.showinfo("Success", "Profile picture updated successfully")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def save_information(self):
        try:
            # Get the information from the entries
            name = self.name_entry.get()
            lastname = self.last_name_entry.get()
            email = self.email_entry.get()
            username = self.username_entry.get()
            phone = self.phone_entry.get()

            # Verify if the username or email already exists, except for the current user
            if fb.verify_others_users(self, username, email):
                messagebox.showerror("Error", "Username or email already exists")
                return
            
            # Save the data in a dictionary
            user_data = {
                "name": name,
                "lastname": lastname,
                "email": email,
                "username": username,
                "phone": phone
            }

            # Update the user's information in the database
            fb.update_collection(self, "users", gv.user_data["id"], user_data)

            # Update the user's information in the global variables
            gv.user_data["name"] = name
            gv.user_data["lastname"] = lastname
            gv.user_data["email"] = email
            gv.user_data["username"] = username

            # Show a success message
            messagebox.showinfo("Success", "Profile updated successfully")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
        