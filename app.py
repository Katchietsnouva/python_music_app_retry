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

root.mainloop()