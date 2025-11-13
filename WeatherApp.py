import sys, requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QLineEdit, QVBoxLayout, QHBoxLayout, QSpacerItem, 
                             QSizePolicy)  
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500,700)

        self.temp_change = QPushButton("Temp Change",self)
        self.type_label = QLabel("Type city:", self)
        self.city_input = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        self.city_label = QLabel(self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.temp_change.setFixedSize(140,60)
        self.count = 1
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Lesson 12")

        hbox = QHBoxLayout()
        
        spacer = QSpacerItem(0,0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox.addItem(spacer)
        hbox.addWidget(self.temp_change)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        
        vbox.addWidget(self.type_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.type_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


        story_id = QFontDatabase.addApplicationFont('PyQt5/Lessons/material/StoryScript-Regular.ttf')
        story_family = QFontDatabase.applicationFontFamilies(story_id)[0]
        story_font = QFont(story_family, 30)
        self.type_label.setFont(story_font)

        unkempt_id = QFontDatabase.addApplicationFont('PyQt5/Lessons/material/Unkempt-Bold.ttf')
        unkempt_family = QFontDatabase.applicationFontFamilies(unkempt_id)[0]
        unkempt_font = QFont(unkempt_family, 30)
        self.city_input.setFont(unkempt_font)
        self.submit_button.setFont(unkempt_font)
        self.temp_change.setFont(unkempt_font) 

        overlockreg = QFontDatabase.addApplicationFont('PyQt5/Lessons/material/Overlock-BoldItalic.ttf')
        overlockreg_family = QFontDatabase.applicationFontFamilies(overlockreg)[0]
        overlockreg_font = QFont(overlockreg_family, 30)
        self.city_label.setFont(overlockreg_font)
        self.description_label.setFont(overlockreg_font)

        overlockbld = QFontDatabase.addApplicationFont('PyQt5/Lessons/material/Overlock-Black.ttf')
        overlockbld_family = QFontDatabase.applicationFontFamilies(overlockbld)[0]
        overlockbld_font = QFont(overlockbld_family, 30)
        self.city_label.setFont(overlockbld_font)
        self.temp_label.setFont(overlockbld_font)
        

        self.type_label.setObjectName("type_label")
        self.city_input.setObjectName("city_input")
        self.city_label.setObjectName("city_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.submit_button.setObjectName("submit_button")
        self.temp_label.setObjectName("temp_label")
        self.temp_change.setObjectName("temp_change")

        self.setStyleSheet("""                           
            
            QWidget{
                    background-color: hsl(0, 49%, 96%);
                }
                
            QLabel{
                    color: hsl(0, 9%, 44%)
           
                }    
            
            QLabel#type_label{
                    font-size: 40px;
                    color: hsl(0, 6%, 20%)       
                }
            QLineEdit#city_input{
                    font-size: 50px;
                    margin: 10px;
                    border: 2px dotted;
                    border-color: hsl(0, 19%, 32%);
                    selection-color: hsl(0, 83%, 33%);
                    color: hsl(0, 45%, 23%);
                }
            QPushButton#submit_button{
                    font-size: 50px;     
                }
            QLabel#emoji_label{
                    font-size: 100px;
                    font-family: Segoe UI Emoji;      
                }
            QLabel#city_label{
                    margin: 10px;
                    font-weight: 200;
                    font-size: 50px; 
                }
            QLabel#description_label{
                    font-size: 40px;
                    font-weight: 300;     
                }
            QLabel#temp_label{
                    font-size: 60px;
                    font-weight: 600;     
                }
            QPushButton#submit_button{
                    border: 2.5px solid;
                    border-color: hsl(0, 5%, 45%);
                    background-color: hsl(0, 13%, 57%);
                    border-radius: 15px;           
                }
            QPushButton#submit_button:hover{
                    border: 2px solid;
                    border-color: hsl(0, 10%, 32%);
                    background-color: hsl(10, 13%, 57%);
                    border-radius: 15px;           
                }
                           
            QPushButton#temp_change{
                    font-size: 20px;
                    border: 2.5px solid;
                    border-color: hsl(0, 10%, 58%);
                    background-color: hsl(0, 20%, 70%);
                    border-radius: 15px;     
                }
            QPushButton#temp_change:hover{
                    border: 2px solid;
                    border-color: hsl(60, 10%, 32%);
                    background-color: hsl(10, 13%, 57%);
                    border-radius: 15px;     
                }
        """)

        self.submit_button.clicked.connect(self.get_weather)
        self.temp_change.clicked.connect(self.counter)

    def get_weather(self, data):
        api_key = 'YOUR_API' 
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            responce = requests.get(url)
            responce.raise_for_status()
            data = responce.json()

            if data['cod'] == 200:
                self.city_label.setText(data['name'])
                self.weather_set(data)
        except requests.exceptions.HTTPError as http_error:
            match responce.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input") 
                case 401:
                    self.display_error("Unauthorized\nInvalid API key") 
                case 403:
                    self.display_error("Forbidden\nAccess is denied") 
                case 404:
                    self.display_error("Not Found\nCity not found") 
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later") 
                case 502:
                    self.display_error("Bad Gateway\nInvalid responce from the server") 
                case 503:
                    self.display_error("Service Unavailble\nServer is down") 
                case 504:
                    self.display_error("Gateway Timeout\nNo responce from the server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")
                    
        except requests.exceptions.ConnectionError:
            self.city_label.setText("Connection Error\nPlease check your internet connection")
        
        except requests.exceptions.Timeout:
            self.city_label.setText("Timeout Error\nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.city_label.setText("Too many Redirects\nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.city_label.setText(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.description_label.setText("")
        self.emoji_label.setText("")
        self.city_label.setText("")
        self.temp_label.setStyleSheet("font-weight: 600;"
                                      "font-size: 40px;")
        self.temp_label.setText(message)

    def weather_set(self, data):
        self.temp_label.setStyleSheet("font-size: 60px;")
        self.weather_data = data

        self.temp_data()
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.emoji_label.setText(self.weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    def weather_emoji(data, weather_id):
        match weather_id:
            case _ if 200 <= weather_id <= 232:
                return "⛈"
            case _ if 300 <= weather_id <= 321:
                return "💧"
            case _ if 500 <= weather_id <= 531:
                return "🌧"
            case _ if 600 <= weather_id <= 622:
                return "🌨"
            case _ if weather_id == 701:
                return "🌫"
            case _ if weather_id == 711:
                return "☁"
            case _ if weather_id == 721:
                return "🌫"
            case _ if weather_id == 731:
                return "⏳"
            case _ if weather_id == 741:
                return "🌁"
            case _ if weather_id == 751:
                return "🌫"
            case _ if weather_id == 761:
                return "🌋"
            case _ if weather_id == 771:
                return "⛈"
            case _ if weather_id == 781:
                return "🌪"
            case _ if weather_id == 800:
                return "☀"
            case _ if 801 <= weather_id <= 804:
                return "🌤"
            case _:
                return ""

    def temp_data(self):
        if not hasattr(self, 'weather_data') or not self.weather_data:
            self.temp_label.setStyleSheet("font-size: 40px;")
            self.temp_label.setText("Please enter a city")
            self.count = 1
            return
          
        try:
            self.temperature_K = self.weather_data['main']['temp']
            self.temperature_C = self.temperature_K - 273.15
            self.temperature_F = (self.temperature_K * 9/5 ) - 459.67

        except KeyError:
            self.temp_change.setText("Error: Temperature data is missing in API response.")
            self.weather_data = None
            self.count = 1
            return
        
        match self.count:
            case 1:
                self.temp_change.setStyleSheet("font-size: 35px;")
                self.temp_change.setText("Celsium")
                return self.temp_label.setText(f"{self.temperature_C:.1f}°C")
            case 2:
                self.temp_change.setStyleSheet("font-size: 28px;")
                self.temp_change.setText("Fahrenheit")
                return self.temp_label.setText(f"{self.temperature_F:.0f}°F")
            case 3:
                self.count = 0
                self.temp_change.setStyleSheet("font-size: 40px;")
                self.temp_change.setText("Kelvin")
                return self.temp_label.setText(f"{self.temperature_K:.0f}°K")

    def counter(self):
        self.count+= 1
        self.temp_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())