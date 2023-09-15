# importing modules
from tkinter import *
import customtkinter
import pygame
# from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window

print('hi')
root.title('Nouva Music')
root.geometry('400x480')
pygame.mixer.init()

list_of_songs = ['nouvamusic\Feelings_7.1_3.1.mp3','nouvamusic\Hard Trap Variant.mp3','nouvamusic\Playful EDM_2.mp3','nouvamusic\Serum_6.mp3','nouvamusic\Sing song_6.mp3','nouvamusic\Vacation_6.mp3','nouvamusic\You dont recognise my face_4.mp3',]
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

play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

# pause_button = customtkinter.CTkButton(master=root, text='||', command=pause_music)
# pause_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)


skip_f_button = customtkinter.CTkButton(master=root, text='>', command=skip_f, width=2)
skip_f_button.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)

skip_b_button = customtkinter.CTkButton(master=root, text='<', command=skip_b, width= 2)
skip_b_button.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to = 1, command=volume, width = 210)
slider.place(relx=0.5, rely=0.78, anchor=customtkinter.CENTER)


root.mainloop()