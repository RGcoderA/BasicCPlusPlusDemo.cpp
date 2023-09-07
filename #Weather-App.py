#Weather-App
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#Search Box

search_frame=Frame(root,bg="white")
search_frame.place(x=0,y=0,width=900,height=50)

search_entry=Entry(search_frame,font=("times new roman",15),bg="lightgray")
search_entry.grid(row=0,column=0,padx=10,pady=10)

search_button=Button(search_frame,text="Search",font=("times new roman",15),bg="lightblue",fg="white",cursor="hand2")
search_button.grid(row=0,column=1,padx=10,pady=10)

root.mainloop()

