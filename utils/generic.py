import bcrypt
from PIL import Image, ImageTk
import requests
import time

def read_image(image_path, size):
    # Read the image and resize it
    return ImageTk.PhotoImage(Image.open(image_path).resize(size, Image.ADAPTIVE))

def read_image_from_url(url, size):
    # Read the image from the url and resize it
    return ImageTk.PhotoImage(Image.open(requests.get(url, stream=True).raw).resize(size, Image.ADAPTIVE))

def center_window(window, width, height):
    # Center the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    return window.geometry(f"{width}x{height}+{x}+{y}")

def get_font_awesome():
    # Get the font awesome
    return "Font Awesome 5 Free"

def encrypt_password(password):
    # Encrypt the password
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def decrypt_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)