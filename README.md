# Weather Checker Bot

## Group Members
- Begimai
- Aruuke
- Muslima

## Project Description
A Telegram bot that provides real-time weather information for any city in the world. The bot also gives clothing advice based on the current temperature.

## Problem Statement
People often need quick access to weather information without opening browsers or apps. Also, many people don't know what to wear based on the weather. Our bot solves both problems by delivering weather data and outfit recommendations instantly through Telegram.

## Solution Overview
We created a Telegram bot using Python that:
- Fetches real-time weather data from OpenWeatherMap API
- Allows users to share their location or enter a city name manually
- Shows temperature, feels like temperature, and weather description
- Gives smart clothing advice based on the current temperature

## Technologies Used
- Python 3.14
- aiogram 
- OpenWeatherMap API
- requests library
- asyncio

## Instructions to Run
1. Clone the repository: git clone https://github.com/samiluranov24-coder/weather-bot.git
2. Install dependencies: pip install aiogram requests
3. Add your tokens in bot.py: TOKEN and API_KEY
4. Run the bot: py bot.py

## Key Features
- Get weather by sharing your location
- Search weather by city name manually
- Shows temperature and feels like temperature
- Shows weather description
- Smart clothing advice based on temperature
- Supports cities worldwide
