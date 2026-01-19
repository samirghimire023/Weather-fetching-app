import requests


# Get API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Check if API key exists
if not API_KEY:
    print("Error: API key not found. Please set OPENWEATHER_API_KEY.")
    exit()

# Ask user for city
city = input("Enter city name: ")

# Build the API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request to API
response = requests.get(url)

# Convert JSON to Python dictionary
data = response.json()

#Error handling
if data.get("cod")  != 200:
    print("Error:", data.get("message")) #print error message if city not found
    exit() #stop the program safely if city not found

temperature = data['main']['temp']
print(f"Temperature in {city}: {temperature}°C")

humidity = data['main']['humidity']
print(f"Humidity in {city}: {humidity}%")

description = data['weather'][0]['description']
print(f"Weather description in {city}: {description}")

feels_like = data['main']['feels_like']
print(f"Feels like in {city}: {feels_like}°C")