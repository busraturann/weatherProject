import requests
from tkinter import *
from tkinter import messagebox
import time

def showweather():
    api_key = "59f9bf749b90b58eed269044d650f9fa"
    city_name = city_entry.get()
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    weather_data = requests.get(weather_url)
    response = weather_data.json()

    if len(city_name) == 0:
        messagebox.showinfo(title="Error!", message="Please enter information.")
    else:
        messagebox.showinfo(title=f"{city_name}", message=f"Hava sıcaklığı {response['main']['temp']} Kelvin")


window = Tk()
window.title("Weather Project")
window.config(pady=30, padx=30)

# picture
picture = PhotoImage(file="clouds.png", width=300, height=200)
label1 = Label(image=picture, pady=50, anchor="center")
label1.pack()

city_label = Label(text="Enter your city", font=25)
city_label.pack()
city_entry = Entry(width=40)
city_entry.pack()

fetch_button = Button(text="Fetch Weather", command=showweather)
fetch_button.pack()


window.mainloop()
