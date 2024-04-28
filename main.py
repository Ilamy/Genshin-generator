import tkinter as tk
from tkinter import *
import customtkinter as ctk
import random
import sqlite3
import os
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x1000")


conn = sqlite3.connect("Genshin.db")

cursor = conn.cursor()

def load_image(path):
    try:
        with Image.open(path) as img:
            return ImageTk.PhotoImage(img)
    except IOError as e:
        print(f"Error opening image file: {e}")
        return None

def update_display():
    character = generate()
    character_name = character.split('.')[0]
    character_info = getCharactersInfo(character_name)
    image_path = os.path.join(r"C:\Users\adaml\Desktop\Genshin generator\images", character)
    photoimage = load_image(image_path)
    
    if photoimage: 
        label1.config(image=photoimage)
        label1.image = photoimage

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

def getCharactersInfo(character):
    sql="SELECT * FROM Characters WHERE name = :name "
    cursor.execute(sql, {'name': character})
    character_info = cursor.fetchone()
    return character_info


frame1 = ctk.CTkFrame(master = app, width = 450, height = 200) 
frame1.pack(pady = 20 ) 
  
button1 = ctk.CTkButton(frame1,text="Generate", command=update_display) 
button1.pack(pady=20) 
 
character = generate()
image_path = os.path.join(r"C:\Users\adaml\Desktop\Genshin generator\images", character)
photoimage = load_image(image_path)

label1 = tk.Label(app, image=photoimage if photoimage else None)
label1.place(x=0, y=100)
label1.image = photoimage
    
app.mainloop()