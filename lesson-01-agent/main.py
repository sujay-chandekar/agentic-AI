from tools.calculator import calculator
from tools.weather import getWeather

def ai_agent(input_text):
    input_text  = input_text.lower()
    if "calculate" in input_text:
        ans = calculator(10, 5, "add")
        return f"The result of the calculation is: {ans}"
    elif "weather" in input_text:
        city = input_text.split(" ")[-1].strip()
        weather_info = getWeather(city)
        return f"The weather in {city} is: {weather_info}"


response = ai_agent("what is the weather in pune ?")

print(response)