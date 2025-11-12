# ☁️ Simple Weather App (PyQt5)
### This is a desktop weather forecasting application built using Python and PyQt5.

__This project serves as my *final work*, concluding the course of studying the [PyQt5](https://github.com/Wivoid/edu/tree/main/PyQt5) framework.
In my [edu repository](https://github.com/Wivoid/edu), you can find a detailed review of the entire development process and other learning materials.__

## 🚀 Getting Started
__To run the application, you must install dependencies and configure the OpenWeatherMap API key.__

### 1. Requirements and API Key Acquisition
__The application relies on external weather data, requiring a unique API key.__
1. __Install Python__: Ensure you have Python 3.x installed on your system.
2. __Get Your Key__:
     * Navigate to the official [OpenWeatherMap](https://openweathermap.org/) website.
     * Create a free account.
     * Copy the generated API key from the "API keys" section of your profile.
  
### Installation and Setup
__Clone the repository and install the necessary libraries within a virtual environment.__

```# Clone the project```
```git clone https://github.com/Wivoid/WeatherApp```
```cd <WeatherApp>```
### Create and activate a virtual environment
```python -m venv venv```
```source venv/bin/activate  # Use .\venv\Scripts\activate on Windows```

## Install required libraries (PyQt5 and requests)
```pip install -r requirements.txt```

## 3. API Key Configuration
__The application will not function until you insert your personal key.__

* Open the main application file `weather_app.py`.
* Locate the `get_weather` function (the method responsible for data requests).
* Replace the placeholder with your actual OpenWeatherMap key:
  
  ```api_key = 'YOUR_API_KEY_HERE' # Paste your actual key here```

## 4. Running the Application
__With your environment active and the key configured, launch the application__:

```python weather_app.py```
