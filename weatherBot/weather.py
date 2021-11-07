import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

print("यस अनुप्रयोगमा स्वागत छ")

def first_function(entry):
	print("यो प्रविष्टि हो:", entry)

def second_function(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'शहर: %s \nमौसम अवस्था: %s \nतापमान (°F): %s' % (name, desc, temp)
	except:
		final_str = 'त्यो जानकारी पुन: प्राप्त गर्नमा समस्या भयो'

	return final_str

def final_function(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = second_function(weather)

root = tk.Tk()
root.title('मौसम आवेदन')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='backgrnd.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="मौसम प्राप्त गर्नुस्", font=40, command=lambda: final_function(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()