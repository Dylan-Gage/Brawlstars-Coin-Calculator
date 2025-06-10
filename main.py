import customtkinter as ctk
from widgets import CoinApp

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
app = CoinApp(root)
root.mainloop()
