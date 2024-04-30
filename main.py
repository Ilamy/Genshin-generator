import tkinter as tk
from tkinter import *
import customtkinter as ctk
import random
import sqlite3
import os
from PIL import Image, ImageTk
import PIL

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x1000")


conn = sqlite3.connect("Genshin.db")

cursor = conn.cursor()

def load_image(path, width, height):
    try:
        with Image.open(path) as img:
            img = img.resize((width, height), PIL.Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
    except IOError as e:
        print(f"Error opening image file: {e}")
        return None

def update_display():
    character = generate()
    character_name = character.split('.')[0]
    character_info = getCharacterInfo(character_name)
    image_path = os.path.join(r"C:\Users\adaml\Desktop\Genshin generator\images", character)
    photoimage = load_image(image_path, 450, 900)
    
    if photoimage: 
        label1.config(image=photoimage)
        label1.image = photoimage
        
    label_top_left.configure(text=character_info[0])
    label_top_right.configure(text=character_info[1])
    label_bottom_left.configure(text=character_info[2])
    label_bottom_right.configure(text=character_info[4])
    
def get_file_names(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return []

    file_names = os.listdir(folder_path)
    return file_names

def generate():
    character_list = get_file_names(r"C:\Users\adaml\Desktop\Genshin generator\images")
    character_number = random.randint(0, len(character_list) - 1)
    return character_list[character_number]

def getCharacterInfo(character):
    sql="SELECT * FROM Characters WHERE name = :name "
    cursor.execute(sql, {'name': character})
    character_info = cursor.fetchone()
    return character_info

character = generate()
character_name = character.split('.')[0]
character_info = getCharacterInfo(character_name)

frame1 = ctk.CTkFrame(app, width = 450) 
frame1.pack(expand=True, fill='both')
#frame1.configure(width = 450)

label_top_left = ctk.CTkLabel(frame1, text = "", text_color = "white")
label_top_left.pack(side="top", anchor="nw")

label_top_right = ctk.CTkLabel(frame1, text="", text_color = "white")
label_top_right.pack(side="top", anchor="ne")

button1 = ctk.CTkButton(frame1, text="Generate!", command=update_display) 
button1.pack(anchor='n')

label_bottom_left = ctk.CTkLabel(frame1, text="", text_color = "white")
label_bottom_left.pack(side="bottom", anchor="sw")

label_bottom_right = ctk.CTkLabel(frame1, text="", text_color = "white")
label_bottom_right.pack(side="bottom", anchor = "se")


image_path = os.path.join(r"C:\Users\adaml\Desktop\Genshin generator\images", character)
photoimage = load_image(image_path, 450, 900)

label1 = tk.Label(app, image=photoimage if photoimage else None)
label1.place(x=0, y=100)
label1.image = photoimage

label_top_left.configure(text=character_info[0])
label_top_right.configure(text=character_info[1])
label_bottom_left.configure(text=character_info[2])
label_bottom_right.configure(text=character_info[4])

app.mainloop()