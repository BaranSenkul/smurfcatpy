#made by baransenkul

import tkinter as tk
from tkinter import ttk
import random
import threading
import playsound
import time

def play_sound():
    playsound.playsound("spectre.mp3")

def create_window_with_text(text, font, x, y):
    window = tk.Toplevel(root)
    window.title(text)
    
    label = tk.Label(window, text=text, font=font)
    label.update_idletasks()  # Ensure label is updated to compute its size
  
    window.geometry(f"400x100+{x}+{y}")
    
    label = tk.Label(window, text=text, font=font)
    label.pack()
    return window

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

root = tk.Tk()
root.title("WE LIVE")

# After 4.73 seconds, create the "WE LIVE" window
root.after(4730, create_window_with_text, "WE LIVE", ("bold", 32), random.randint(50, 150), random.randint(50, 150))

# After 1.2 seconds, create the "WE LOVE" window on the middle right side
root.after(5930, create_window_with_text, "WE LOVE", ("bold", 36), root.winfo_screenwidth() - 450, root.winfo_screenheight() // 2 - 100)

# After 1.6 seconds, create the "WE LIE" window with a larger font at the bottom
root.after(6700, create_window_with_text, "WE LIE", ("italic bold", 48), root.winfo_screenwidth() // 2 - 100, root.winfo_screenheight() - 150)

image = tk.PhotoImage(file="sumrfcat.png")

def display_image():
    window_image = tk.Toplevel(root)
    window_image.title("Image")
    
    # Adjust the window size to fit the image
    window_width = image.width()
    window_height = image.height()
    window_x = root.winfo_screenwidth() // 2 - window_width // 2
    window_y = root.winfo_screenheight() // 2 - window_height // 2
    
    window_image.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    
    label_image = tk.Label(window_image, image=image)
    label_image.pack()

root.after(7630, display_image)

root.withdraw()  # Hide the main window
root.mainloop()
