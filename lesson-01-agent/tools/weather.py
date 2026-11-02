def getWeather(city):

    data = {
        "pune":"Sunny, 35°C",
        "mumbai":"Rainy, 30°C",
        "delhi":"Cloudy, 28°C",
    }
    return data.get(city.lower(), "Weather data not available for this city.")
