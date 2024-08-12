import requests

def get_weather(city):
    
    url = f"https://api.popcat.xyz/weather?q={city}"

   
    response = requests.get(url)

    
    if response.status_code == 200:
        weather_data = response.json()

        
        print("Raw Response Data:", weather_data)

        
        if 'location' in weather_data and 'current' in weather_data:
           
            city_name = weather_data['location']['name']

            region = weather_data['location']['region']

            country = weather_data['location']['country']

            temp = weather_data['current']['temperature']

            description = weather_data['current']['description']

            humidity = weather_data['current']['humidity']

            wind_speed = weather_data['current']['wind_speed']


        
            print(f"Weather in {city_name}, {region}, {country}:")

            print(f"Temperature: {temp}°C")

            print(f"Description: {description}")

            print(f"Humidity: {humidity}%")

            print(f"Wind Speed: {wind_speed} km/h")
        else:
            print(f"Unexpected data format in API response: {weather_data}")
    else:
        print(f"Error: Unable to retrieve data for {city}. HTTP Status: {response.status_code}")


city = input("Enter the name of the city: ")
get_weather(city)
