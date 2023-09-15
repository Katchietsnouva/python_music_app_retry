# importing modules
from tkinter import *
import customtkinter
import pygame
# from PIL import Image, ImageTk
from threading import *
import time
import math


# Set customtkinter appearance mode and color theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title('Nouva Music')
root.geometry('400x480')
pygame.mixer.init()

list_of_songs = [
    'nouvamusic/Feelings_7.1_3.1.mp3',
    'nouvamusic/Hard Trap Variant.mp3',
    'nouvamusic/Playful EDM_2.mp3',
    'nouvamusic/Serum_6.mp3',
    'nouvamusic/Sing song_6.mp3',
    'nouvamusic/Vacation_6.mp3',
    'nouvamusic/You dont recognise my face_4.mp3'
]

list_of_covers = []

def play_music():
    pass

def pause_music():
    pass

def skip_f():
    pass

def skip_b():
    pass

def volume(value):
    print(value)

    
def adjust_button_positions(event):
    # Calculate the center of the window's width
    window_width = event.width
    button_x = window_width / 2
    print(window_width)
    print(button_x)


play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
skip_f_button = customtkinter.CTkButton(master=root, text='>', command=skip_f, width=2)
skip_b_button = customtkinter.CTkButton(master=root, text='<', command=skip_b, width=2)
slider = customtkinter.CTkSlider(master=root, from_=0, to=1, command=volume, width=210)
progress = customtkinter.CTkProgressBar(master=root,progress_color='#3777de', border_width= .2, width =250)

play_button.place(x=200, y=336, anchor='center')
skip_f_button.place(x=280, y=336, anchor='center')
skip_b_button.place(x=120, y=336, anchor='center')
slider.place(x=200, y=385, anchor='center')
progress.place(relx=.5, rely=.85, anchor=customtkinter.CENTER)



root.mainloop()



