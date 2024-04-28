import tkinter as tk
import customtkinter as ctk
import random
import sqlite3
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("450x1000")


conn = sqlite3.connect("Genshin.db")

cursor = conn.cursor()

def get_file_names(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return []

    # Get all file names in the folder
    file_names = os.listdir(folder_path)
    return file_names

def generate():
    #random number
    character_number = random.randint(0,11)
    #list of characters
    character_list = get_file_names(r"C:\Users\adaml\Desktop\Genshin generator\images")

    return character_list[character_number]

character = generate().split('.')

def getCharactersInfo(character):
    sql="SELECT * FROM Characters WHERE name = :name "
    
    cursor.execute(sql, {'name': character})
    character_info = cursor.fetchone()
    return character_info

characterinfo = getCharactersInfo(character[0])  

#set image + give infos

app.mainloop()