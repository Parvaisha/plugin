import requests

# Get user input for the city name
city = input("Enter city name: ")

url = f"https://v1.nocodeapi.com/parvaisha08/ow/xRFHRzamGnlGgBQl/byCityName?q={city}"
params = {}
r = requests.get(url=url, params=params)

if r.status_code == 200:
    result = r.json()

    # Extract only the "main" information
    main_data = result.get("main")

    if main_data:
       
        print(f"Temperature: {main_data.get('temp')}°C")
        print(f"Humidity: {main_data.get('humidity')}%")
    else:
        print("Error: 'main' information not found in the response.")
else:
    print(f"Error fetching weather data: {r.status_code}")
