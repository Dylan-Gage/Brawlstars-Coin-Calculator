import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tkinter import Label, Button
from logic import calc_total_coins

class CoinApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x700")
        self.root.title("Brawlstars Coin Calculator")
        

        self.lvl_lower = 1
        self.lvl_upper = 1
        self.gadget = 0
        self.gear = 0
        self.starpower = 0
        self.hypercharge = 0

        self.setup_ui()
        self.setup_frames()
        self.setup_icons()
        self.setup_labels()
        self.setup_buttons()
        
        
    def setup_ui(self):
        self.label = ctk.CTkLabel(self.root, text="Welcome to the Coin Calculator", font=("Segoe UI", 18))
        self.label.pack(pady=20)

    def setup_icons(self):
        self.gadget_icon_img = ctk.CTkImage(light_image=Image.open("C:\\Users\\Dylan\\OneDrive\\Desktop\\Personal Projects\\BrawlStarsCalc\\Images\\gadget_icon.png"),size=(40,40))
        self.gadget_icon = ctk.CTkLabel(self.gadget_frame, image=self.gadget_icon_img,text="")
        self.gadget_icon.grid(row=0,column=0,padx=10)

        self.gear_icon_img = ctk.CTkImage(light_image=Image.open("C:\\Users\\Dylan\\OneDrive\\Desktop\\Personal Projects\\BrawlStarsCalc\\Images\\gear_icon.png"),size=(40,40))
        self.gear_icon = ctk.CTkLabel(self.gear_frame, image=self.gear_icon_img,text="")
        self.gear_icon.grid(row=2,column=0,padx=10)
        
        self.starpower_icon_img = ctk.CTkImage(light_image=Image.open("C:\\Users\\Dylan\\OneDrive\\Desktop\\Personal Projects\\BrawlStarsCalc\\Images\\starpower_icon.png"),size=(40,40))
        self.starpower_icon = ctk.CTkLabel(self.starpower_frame, image=self.starpower_icon_img,text="")
        self.starpower_icon.grid(row=4,column=0,padx=10)

        self.hypercharge_icon_img = ctk.CTkImage(light_image=Image.open("C:\\Users\\Dylan\\OneDrive\\Desktop\\Personal Projects\\BrawlStarsCalc\\Images\\hypercharge_icon.png"),size=(40,40))
        self.hypercharge_icon = ctk.CTkLabel(self.hypercharge_frame, image=self.hypercharge_icon_img,text="")
        self.hypercharge_icon.grid(row=6,column=0,padx=10)
            

    def setup_frames(self):
        self.gadget_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.gadget_frame.pack(pady=20)

        self.gear_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.gear_frame.pack(pady=20)

        self.starpower_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.starpower_frame.pack(pady=20)

        self.hypercharge_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.hypercharge_frame.pack(pady=20)

        self.coin_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.coin_frame.pack(pady=20)

        self.lvl_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.lvl_frame.pack(pady=20)

        self.total_coins_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.total_coins_frame.pack(pady=20)


        

    def setup_labels(self):
        self.coin_lbl = ctk.CTkLabel(self.coin_frame, text="Total Coins: 0", font=("Segoe UI", 14))
        self.coin_lbl.grid(row=8, column=2, padx=10)

        self.lbl1 = ctk.CTkLabel(self.lvl_frame, text=f"{self.lvl_lower}",width=40, font=("Segoe UI", 14))
        self.lbl1.grid(row=0, column=1, padx=5)

        self.lbl2 =  self.lbl2 = ctk.CTkLabel(self.lvl_frame, text=f"{self.lvl_upper}",width=40, font=("Segoe UI", 14))
        self.lbl2.grid(row=0, column=5, padx=5)

        self.gadget_lbl = ctk.CTkLabel(self.gadget_frame, text="Gadget: 0", font=("Segoe UI", 14))
        self.gadget_lbl.grid(row=0, column=2, padx=10)

        self.gear_lbl = ctk.CTkLabel(self.gear_frame, text="Gear: 0", font=("Segoe UI", 14))
        self.gear_lbl.grid(row=2, column=2, padx=10)

        self.starpower_lbl = ctk.CTkLabel(self.starpower_frame, text="Star Power: 0", font=("Segoe UI", 14))
        self.starpower_lbl.grid(row=4, column=2, padx=10)

        self.hypercharge_lbl = ctk.CTkLabel(self.hypercharge_frame, text="Hypercharge: 0", font=("Segoe UI", 14))
        self.hypercharge_lbl.grid(row=6, column=2, padx=10)

        self.level_lbl  = ctk.CTkLabel(self.lvl_frame, text="Level",width=40, font=("Segoe UI", 14))
        self.level_lbl.grid(row=0, column=3, padx=5)

    def setup_buttons(self):
        ctk.CTkButton(self.lvl_frame, text="-", width=40, command=self.dec_lvl_lower).grid(row=0, column=0, padx=5)
        ctk.CTkButton(self.lvl_frame, text="+", width=40, command=self.inc_lvl_lower).grid(row=0, column=2, padx=5)
        ctk.CTkButton(self.lvl_frame, text="-", width=40, command=self.dec_lvl_upper).grid(row=0, column=4, padx=5)
        ctk.CTkButton(self.lvl_frame, text="+", width=40, command=self.inc_lvl_upper).grid(row=0, column=6, padx=5)

        
        ctk.CTkButton(self.gadget_frame, text="-", width=40, command=self.dec_gadget).grid(row=0, column=1)
        ctk.CTkButton(self.gadget_frame, text="+", width=40, command=self.inc_gadget).grid(row=0, column=3)

        ctk.CTkButton(self.gear_frame, text="-", width=40, command=self.dec_gear).grid(row=2, column=1)
        ctk.CTkButton(self.gear_frame, text="+", width=40, command=self.inc_gear).grid(row=2, column=3)

        ctk.CTkButton(self.starpower_frame, text="-", width=40, command=self.dec_starpower).grid(row=4, column=1)
        ctk.CTkButton(self.starpower_frame, text="+", width=40, command=self.inc_starpower).grid(row=4, column=3)

        ctk.CTkButton(self.hypercharge_frame, text="-", width=40, command=self.dec_hypercharge).grid(row=6, column=1)
        ctk.CTkButton(self.hypercharge_frame, text="+", width=40, command=self.inc_hypercharge).grid(row=6, column=3)

        
        ctk.CTkButton(self.total_coins_frame, text="Calculate Coins", width=40, command=self.update_total).grid(row=14, column=3)
    
    def dec_lvl_lower(self):
        if self.lvl_lower > 1:
            self.lvl_lower -= 1
            self.sync_levels()
        self.lbl1.configure(text=self.lvl_lower)

    def inc_lvl_lower(self):
        if self.lvl_lower < 11:
            self.lvl_lower += 1
            self.sync_levels()
        self.lbl1.configure(text=self.lvl_lower)

    def dec_lvl_upper(self):
        if self.lvl_upper > 1:
            self.lvl_upper -= 1
            self.sync_levels()
        self.lbl2.configure(text=self.lvl_upper)

    def inc_lvl_upper(self):
        if self.lvl_upper < 11:
            self.lvl_upper += 1
            self.sync_levels()
        self.lbl2.configure(text=self.lvl_upper)

    def sync_levels(self):
        if self.lvl_lower > self.lvl_upper:
            self.lvl_upper = self.lvl_lower
        elif self.lvl_upper < self.lvl_lower:
            self.lvl_lower = self.lvl_upper
        self.lbl1.configure(text=self.lvl_lower)
        self.lbl2.configure(text=self.lvl_upper)

    def inc_gadget(self):
        if self.gadget < 2:
            self.gadget += 1
        self.gadget_lbl.configure(text=f"Gadget: {self.gadget}")

    def dec_gadget(self):
        if self.gadget > 0:
            self.gadget -= 1
        self.gadget_lbl.configure(text=f"Gadget: {self.gadget}")

    def inc_gear(self):
        if self.gear < 2:
            self.gear += 1
        self.gear_lbl.configure(text=f"Gear: {self.gear}")
    
    def dec_gear(self):
        if self.gear > 0:
            self.gear -= 1
        self.gear_lbl.configure(text=f"Gear: {self.gear}")

    def inc_starpower(self):
        if self.starpower < 2:
            self.starpower += 1
        self.starpower_lbl.configure(text=f"Star Power: {self.starpower}")

    def dec_starpower(self):
        if self.starpower > 0:
            self.starpower -= 1
        self.starpower_lbl.configure(text=f"Star Power: {self.starpower}")
    
    def inc_hypercharge(self):
        if self.hypercharge < 1:
            self.hypercharge += 1
        self.hypercharge_lbl.configure(text=f"Hypercharge: {self.hypercharge}")
    
    def dec_hypercharge(self):
        if self.hypercharge > 0:
            self. hypercharge -= 1
        self.hypercharge_lbl.configure(text=f"Hypercharge: {self.hypercharge}")
        

    

    def update_total(self):
        total = calc_total_coins(self.lvl_lower, self.lvl_upper, self.gadget, self.gear, self.starpower, self.hypercharge)
        self.coin_lbl.configure(text="Total Coins: " + str(total))

