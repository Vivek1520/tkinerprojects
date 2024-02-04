import tkinter as tk
from PIL import Image, ImageTk
import requests


def get_weather():
    api_key = "31460e3c08da677259eee13ef17c5cf7"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = city_entry.get()

    try:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(base_url, params=params)
        weather_data = response.json()
        if weather_data["cod"] != "404":
            temperature = weather_data["main"]["temp"]
            pressure = weather_data["main"]["pressure"]
            humidity = weather_data["main"]["humidity"]
            weather_info = f"City: {city}\nTemperature: {temperature}°C\nPressure: {pressure}hPa\nHumidity: {humidity}%"
            weather_label.config(text=weather_info)
        else:
            weather_label.config(text="Weather data not available")
    except:
        weather_label.config(text="Failed to fetch weather data")


root = tk.Tk()
root.title("Weather App")
root.minsize(width=400, height=650)


root.columnconfigure(1, weight=2)
label = tk.Label(text="Weather App", font=("Arial", 18, "bold"), fg="#f5b642")
label.grid(column=1, row=1,pady=40)

# Open the image file
image = Image.open("weather.png")

resized_image = image.resize((200, 200))

tk_image = ImageTk.PhotoImage(resized_image)


image_label = tk.Label(image=tk_image)
image_label.grid(column=1, row=2, pady=(30, 0))

city_entry = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", justify="center")
city_entry.insert(0, "Enter city name")  # Set the default text or placeholder
city_entry.grid(column=1, row=3,pady=40)

button = tk.Button(root, text="Get Weather", command=get_weather, bg="lightblue",font=("Arial", 12, "bold"))
button.grid(column=1, row=4)

weather_label = tk.Label(root, text="", font=("Arial", 12, "bold"),fg="#f5b642")
weather_label.grid(column=1, row=5,pady=20)

root.mainloop()