#-----------
# smurfcatpy
#----------
# made by baransenkul
#---READ---
# If you are going to post this online, modify it or anything else. Give credit to @BaranSenkul
# https://www.tiktok.com/@baransenkul
# this script has been lisenced under the MIT Lisence.
# I kinda suck at documenting my own code, So have fun tinkering!
#----------

import tkinter as tk
from tkinter import ttk
import random
import threading
from playsound import playsound

def play_sound():
    playsound("spectre.mp3")

def create_window_with_text(text, font, x, y):
    window = tk.Toplevel(root)
    window.title("Public ver. Made by BaranSenkul")
    
    label = tk.Label(window, text=text, font=font)
    label.update_idletasks()  # Ensure the text is updated to compute its size
  
    window.geometry(f"400x100+{x}+{y}")
    
    label = tk.Label(window, text=text, font=font)
    label.pack()
    return window

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

root = tk.Tk()
root.title("Public ver. Made by BaranSenkul")

root.after(5130, create_window_with_text, "WE LIVE", ("Verdana", 32), random.randint(50, 150), random.randint(50, 150))
root.after(5930, create_window_with_text, "WE LOVE", ("Verdana", 36), root.winfo_screenwidth() - 450, root.winfo_screenheight() // 2 - 100)
root.after(6950, create_window_with_text, "WE LIE", ("Verdana", 48), root.winfo_screenwidth() // 2 - 100, root.winfo_screenheight() - 165)

image = tk.PhotoImage(file="smurfcat.png")

def display_image():
    window_image = tk.Toplevel(root)
    window_image.title("Image")
    window_width = image.width()
    window_height = image.height()
    window_x = root.winfo_screenwidth() // 2 - window_width // 2
    window_y = root.winfo_screenheight() // 2 - window_height // 2
    
    window_image.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
    
    label_image = tk.Label(window_image, image=image)
    label_image.pack()

root.after(7730, display_image)

root.withdraw() 
root.mainloop()

# https://www.tiktok.com/@baransenkul
