import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def formatResponse(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTempature: %s' % (name, desc, temp)
    
    except:
        final_str = "There was a problem retrieving the information..."

    return final_str

def getWeather(city):
    weather_key = '1e6683eb8a34c5c89685410584636386'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = formatResponse(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='bg.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='lightgray', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 12))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Test button", font=40, command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lowerFrame = tk.Frame(root, bg='lightgray', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowerFrame, font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()