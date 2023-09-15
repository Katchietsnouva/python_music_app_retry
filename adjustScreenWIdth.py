import tkinter as tk

def on_resize(event):
    new_width = event.width
    label.config(text=f"Screen Width: {new_width}")
    button_x = new_width / 2
    frame.place(x=button_x, y=100, anchor="center")
    print(f"Altered Screen Width: {new_width}")

def update_final_width():
    final_width = root.winfo_width()
    print(f"Final Screen Width: {final_width}")

root = tk.Tk()
root.title("Resizable Window Example")
root.geometry("400x300")

label = tk.Label(root, text="Screen Width: ")
label.pack()

frame = tk.Frame(root, width=100, height=50, bg="blue")
frame.pack()

root.bind("<Configure>", on_resize)

# After a short delay (1000 milliseconds), update the final width
root.after(1000, update_final_width)

root.mainloop()
