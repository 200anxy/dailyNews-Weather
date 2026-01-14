
from dotenv import load_dotenv
import os
from GetNews import textOutput
from GetWeather import getWeatherString
load_dotenv()
x=1

def concatMSG():
    return "Good Morning!\n" + getWeatherString()+"\n"+ textOutput() 
# print(concatMSG())