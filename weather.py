import requests

def weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        data = requests.get(url).json()

        current = data['current_condition'][0]

        temp = current['temp_C']
        desc = current['weatherDesc'][0]['value']

        return f"Temperature: {temp}°C\nCondition: {desc}"

    except Exception as e:
        return f"Error: {e}"
'''while True:
    command = input("You: ").lower()

    if command == "weather":
        city = input("Enter city: ")
        print(weather(city))

    elif command == "exit":
        break
    
weather("chennai")
'''
