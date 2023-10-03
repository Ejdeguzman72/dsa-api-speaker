import os 
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import json
import requests
from flask_caching import Cache

config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEIOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

def convertKelvinToFahrenheit(kelvin):
    return round((kelvin - 273.15) * 1.8 + 32)

def getDadJoke():
    try:
        url = "https://dad-jokes.p.rapidapi.com/random/joke"

        headers = {
        "X-RapidAPI-Key": "3b215bec64mshf11f807f911e339p154028jsn48a563f5adfd",
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:

            response_dict = json.loads(response.text)
        else:
            return "Error in retrieving response"   
    except:
        return "An error occurred"
    return response_dict

def get_city_temperature(city):
    try: 
        api_key = "ba956bf9768422b2b6140506ad90c573"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data))
            name = data['name']
            longitude = data['coord']['lon']
            latitude = data['coord']['lat']
            minTemp = data['main']['temp_min']
            temp = data['main']['temp']
            maxTemp = data['main']['temp_max']
            descr = data['weather'][0]['description']
            windspeed = data['wind']['speed']

            weatherDict = {
                "City": name,
                "Coordinates": str(latitude) + ", " + str(longitude),
                "Minimum Temperature": convertKelvinToFahrenheit(minTemp),
                "Current Temperature": convertKelvinToFahrenheit(temp),
                "Max Temperature": convertKelvinToFahrenheit(maxTemp),
                "Wind Speed": windspeed,
                "Description:": descr
            }
        else:
            return "Error in retrieving response"
    except:
        return "An error occurred"
    return weatherDict

def callTopHeadlinesNewsClient():
    try:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def retrievePoliticalNews():
    try:
        url = f'https://newsapi.org/v2/everything?q=politics&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def retrieveSportsNews():
    try:
        url = f'https://newsapi.org/v2/everything?q=sports&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def retrieveFinanceNews():
    try:
        url = f'https://newsapi.org/v2/everything?q=finance&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def retrieveTechnologyNews():
    try:
        url = f'https://newsapi.org/v2/everything?q=technology&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles
    
def retrieveBusinessNews():
    try:
        url = f'https://newsapi.org/v2/everything?q=business&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def searchHeadlinesNewsClient(topic):
    try:
        url = f'https://newsapi.org/v2/everything?q={topic}&apiKey=5f54e99a747b4269bbe98e3aca7cb29b'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return articles

def searchStockInfo(stock):
    try:
        url = f'https://api.stockdata.org/v1/data/quote?symbols={stock}&api_token=PC5Mi5Z8YMTCQSaSKh03g7naP50yhvS2AZAtR7ou'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            stocks_list = data['data']
        else:
            return "Error in returning response"
    except:
        return "An error occurred"
    return stocks_list

def findEvents():
    url = f''

@app.get("/app")
@cache.cached(timeout=50)
def home():
    return "Hello World"

@app.route("/app/weather/city/<string:name>", methods=["GET"])
@cache.cached(timeout=50)
def getCityWeather(name):
    return get_city_temperature(name)

@app.route("/app/jokes/joke", methods=["GET"])
@cache.cached(timeout=50)
def getJoke():
    return getDadJoke()

@app.route("/app/news/all", methods=['GET'])
@cache.cached(timeout=50)
def getNews():
    return callTopHeadlinesNewsClient()

@app.route("/app/news/sports/all")
@cache.cached(timeout=50)
def getSportsNews():
    return retrieveSportsNews()

@app.route("/app/news/finance/all")
@cache.cached(timeout=50)
def getFinanceNews():
    return retrieveFinanceNews()

@app.route("/app/news/politics/all")
@cache.cached(timeout=50)
def getPoliticalNews():
    return retrievePoliticalNews()

@app.route("/app/news/technology/all")
@cache.cached(timeout=50)
def getTechnologyNews():
    return retrieveTechnologyNews()

@app.route("/app/news/business/all")
@cache.cached(timeout=50)
def getBusinessNews():
    return retrieveBusinessNews()

@app.route("/app/news/search/<string:topic>", methods=['GET'])
@cache.cached(timeout=50)
def searchNews(topic):
    return searchHeadlinesNewsClient(topic)

@app.route("/app/stocks/search/<string:stock>", methods=['GET'])
@cache.cached(timeout=50)
def getStockInfo(stock):
    print(stock)
    return searchStockInfo(stock)