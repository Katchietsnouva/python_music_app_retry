# importing modules
from tkinter import *
import customtkinter
import pygame
from PIL import Image, ImageTk
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

n=0
list_of_songs = [
    'nouvamusic/Feelings_7.1_3.1.mp3',
    'nouvamusic/Hard Trap Variant.mp3',
    'nouvamusic/Playful EDM_2.mp3',
    'nouvamusic/Serum_6.mp3',
    'nouvamusic/Sing song_6.mp3',
    'nouvamusic/Vacation_6.mp3',
    'nouvamusic/You dont recognise my face_4.mp3'
]

list_of_covers = [
    'images\\image (1).jpeg',
    'images\\image (1).jpg',
    'images\\image (1).webp',
    'images\\image (2).jpeg',
    'images\\image (2).jpg',
    'images\\image (3).jpeg',
    'images\\image (3).jpg',
    'images\\image (4).jpeg'
]

def get_album_cover(song_name, n):
    image1 = Image.open(list_of_covers[n])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)

    label1 = Label(root, image=load)  # Use the Label widget from tkinter
    label1.image = load
    label1.place(relx=.19, rely=.06)

    stripped_string = song_name[6:-4]  # This is to exclude the other characters
    # 6       :      -4
    # Example: 'music/ | City | .wav'
    # This works because the music will always be between those 2 values

    song_name_label = Label(text=stripped_string, bg='#222222', fg='white')  # Use Label from tkinter
    song_name_label.place(relx=.4, rely=.6)

def progress():
    a=pygame.mixer.Sound(f'{list_of_songs[n]}')
    song_len = a.get_length() *3
    for i in range (0, math.ceil(song_len)):
        time.sleep(.3)
        progressbar.set(pygame.mixer.music.get_pos()/1000000)
def threading():
    t1=Thread(target=progress)
    t1.start()

def play_music():
    # threading()
    global n
    
    current_song = n
    if n > 2:
        n = 0
    song_name = list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)  # Adjust the volume here
    get_album_cover(song_name, n)

    print('PLAY')
    n += 1

    
    # Update the progress bar while the music is playing
    while pygame.mixer.music.get_busy():
        progress = pygame.mixer.music.get_pos() / 1000  # Get progress in milliseconds
        progressbar.set(progress / (a.get_length() * 3))  # Update the progress bar
        time.sleep(0.1)  # Sleep for a short interval to avoid busy-waiting




def pause_music():
    pass

def skip_f():
    pass

def skip_b():
    pass

def volume(value):
    pygame.mixer.music.set_volume(value)
  
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
progressbar = customtkinter.CTkProgressBar(master=root,progress_color='#77de37', border_width= .2, width =250)

play_button.place(relx=.5, y=336, anchor=customtkinter.CENTER)
skip_f_button.place(relx=.7, y=336, anchor=customtkinter.CENTER)
skip_b_button.place(relx=.3, y=336, anchor=customtkinter.CENTER)
slider.place(relx=.5, y=385, anchor=customtkinter.CENTER)
progressbar.place(relx=.5, rely=.85, anchor=customtkinter.CENTER)

root.mainloop()



