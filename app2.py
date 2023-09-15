import tkinter as tk

def get_screen_width():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    root.destroy()
    return screen_width

def display_gui(screen_width):
    root = tk.Tk()
    root.title("Screen Width Display")
    label = tk.Label(root, text=f"Screen Width: {screen_width}")
    label.pack(padx=20, pady=20)
    root.mainloop()

if __name__ == "__main__":
    screen_width = get_screen_width()
    print(f"Screen Width: {screen_width}")
    display_gui(screen_width)
