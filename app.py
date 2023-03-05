from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Enter API key
API_KEY = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    country_code = request.form['country_code']

    # Create the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}"

    # Make the API request
    response = requests.get(url)

    # Parse the response
    data = json.loads(response.text)


    # Return the weather information
    return render_template('weather.html', city=city, country_code=country_code,
                           description=data['weather'][0]['description'], 
                           temperature=data['main']['temp'], 
                           humidity=data['main']['humidity'], 
                           wind_speed=data['wind']['speed'])
