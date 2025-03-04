import pyautogui
import customtkinter as ctk
from customtkinter import CTkFont

###################################
# ADD THIS NEW GLOBAL VARIABLE
###################################
overlay_window = None

###################################
# ADD A NEW FUNCTION TO COPY THE SELECTED COLOR
###################################
def copy_color():
    root.clipboard_clear()
    root.clipboard_append(color_label.cget("text"))

def pick_color_from_screen():
    global overlay_window
    overlay_window = ctk.CTkToplevel(root)

    ###################################
    # We remove the "-fullscreen" attribute
    ###################################
    overlay_window.overrideredirect(True)
    overlay_window.attributes('-topmost', True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    overlay_window.geometry(f"{screen_width}x{screen_height}+0+0")

    overlay_window.configure(fg_color="black")  
    overlay_window.attributes('-alpha', 0.3)

    overlay_window.configure(cursor="crosshair")

    overlay_window.bind("<Button-1>", capture_screen_color)

###################################
# UPDATE capture_screen_color TO TAKE EVENT
###################################
def capture_screen_color(event):
    global overlay_window
    x, y = event.x_root, event.y_root

    r, g, b = pyautogui.screenshot().getpixel((x, y))
    hex_color = f"#{r:02x}{g:02x}{b:02x}"

    ###################################
    # DESTROY THE OVERLAY WINDOW
    ###################################
    overlay_window.destroy()
    overlay_window = None

    color_label.configure(text=f"Selected Color: {hex_color}", fg_color=hex_color)

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("400x300")
root.title("Color Picker")

###################################
# PROFESSIONAL-STYLE TOP FRAME/HEADER
###################################
header_frame = ctk.CTkFrame(master=root, corner_radius=10)
header_frame.pack(pady=(20, 10), padx=20, fill="x")

title_font = CTkFont(family="Arial", size=18, weight="bold")
title_label = ctk.CTkLabel(
    master=header_frame,
    text="Color Picker",
    font=title_font
)
title_label.pack(pady=10)

###################################
# MAIN CONTENT FRAME
###################################
main_frame = ctk.CTkFrame(master=root, corner_radius=10)
main_frame.pack(padx=20, fill="both", expand=True)

screen_pick_button = ctk.CTkButton(
    master=main_frame,
    text="Pick Color from Screen",
    command=pick_color_from_screen,
    corner_radius=8,
    height=32
)
screen_pick_button.pack(pady=(15, 10))

color_label = ctk.CTkLabel(
    master=main_frame,
    text="No color selected",
    width=200,
    height=40,
    corner_radius=6
)
color_label.pack(pady=(0, 15))

###################################
# ADD A NEW BUTTON TO COPY THE COLOR
###################################
copy_button = ctk.CTkButton(
    master=main_frame,
    text="Copy Color",
    command=copy_color,
    corner_radius=8,
    height=32
)
copy_button.pack(pady=(0, 20))

root.mainloop()
