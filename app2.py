import tkinter as tk

def get_screen_width():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    root.destroy()
    return screen_width

def display_gui(screen_width):
    def on_resize(event):
        new_width = event.width
        label.config(text=f"Screen Width: {new_width}")
        print(f"Altered Screen Width: {new_width}")

    root = tk.Tk()
    root.title("Screen Width Display")
    
    label = tk.Label(root, text=f"Screen Width: {screen_width}")
    label.pack(padx=20, pady=20)

    root.bind("<Configure>", on_resize)
    root.mainloop()

if __name__ == "__main__":
    screen_width = get_screen_width()
    print(f"Initial Screen Width: {screen_width}")
    display_gui(screen_width)
