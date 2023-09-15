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











root.mainloop()