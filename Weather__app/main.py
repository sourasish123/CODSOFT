from tkinter import*
from tkinter import  ttk
import requests

def data_get():
    city = city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q={city}&appid=20a01944eda34a13f4a4dcecfff77197").json()


    w_label1.config(text=data["Weather"][0]["main"])
    wb_label1.config(text=data["Weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])




win = Tk()
win.title("WEATHER APP")
win.config(bg="grey")
win.geometry("500x600")

name_label = Label(win,text="WEATHER  REPORT",font=("Microsoft YaHei",20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name= StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="WEATHER  REPORT",values=list_name,font=("Microsoft YaHei",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

Done_button=Button(win,text="CHECK",font=("Time New Roman",15,"bold"),command=data_get)
Done_button.place(x=200,y=190,height=50,width=100)

w_label = Label(win,text="Weather Climate",font=("arial",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="",font=("arial",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("arial",17))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",font=("arial",17))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature",font=("arial",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",font=("arial",20))
temp_label1.place(x=250,y=400,height=50,width=210)

pre_label = Label(win,text="Pressure",font=("arial",20))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1 = Label(win,text="",font=("arial",20))
pre_label1.place(x=250,y=470,height=50,width=210)


win.mainloop()