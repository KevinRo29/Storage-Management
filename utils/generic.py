from PIL import Image, ImageTk

def read_image (image_path, size):
    # Read the image and resize it
    return ImageTk.PhotoImage(Image.open(image_path).resize(size, Image.ADAPTIVE))

def center_window (window, width, height):
    # Center the window
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    return window.geometry(f"{width}x{height}+{x}+{y}")