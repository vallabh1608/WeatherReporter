import requests
import pyttsx3
import json

read_out=pyttsx3.init()


while(True):
    city = input("Enter city name: ")
    if(city=="none"):
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=f5f54fbcf1214bc98f670700241701&q={city}"

    r = requests.get(url)

    wdict = json.loads(r.text)
    print("Place:", wdict["location"]["name"] + "," + wdict["location"]["region"] + "," + wdict["location"]["country"],
          "\nlocaltime:", wdict["location"]["localtime"], "\nTemparature:", wdict["current"]["temp_c"], "\nweather:",
          wdict["current"]["condition"]["text"], "\nHumidity:", wdict["current"]["humidity"])
    read_out.say(f"The weather in {city} is"+wdict["current"]["condition"]["text"])

    read_out.runAndWait()

    ch=input(f"Would you like to dive deeper into the weather of {city}? if so enter 'yes' or esle 'no'")
    if(ch=="yes"):
        print(r.text)

    read_out.say("Curious about weather in more cities? Type 'city name' if you want more info, or 'none' to finish: ")
    read_out.runAndWait()







