# 🌦 Weather API

This is a **Weather API** built with Django and Django REST Framework. It allows users to fetch real-time weather data based on city names.

## 🚀 Features
- Get real-time weather data
- Fetch data by city name
- Caching for optimized performance
- Authentication with API keys (if enabled)
- Scheduled email notifications (optional)

## 🛠 Tech Stack
- **Backend:** Django, Django REST Framework
- **Data Source:** OpenWeather API
- **Caching:** Redis (optional)
- **Deployment:** Render / Railway / Fly.io (optional)

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/ASILBEKasilbek/Weather-API.git
$ cd Weather-API
```

### 2️⃣ Create a Virtual Environment & Activate it
```sh
$ python -m venv venv
$ source venv/bin/activate  # Mac & Linux
$ venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your API key:
```env
OPENWEATHER_API_KEY=your_api_key_here
```

### 5️⃣ Run Migrations & Start Server
```sh
$ python manage.py migrate
$ python manage.py runserver
```

## 🔍 API Endpoints

### 🔹 Get Weather by City Name
**Request:**
```http
GET /api/weather?city=London
```
**Response:**
```json
{
  "city": "London",
  "temperature": "15°C",
  "description": "Partly Cloudy",
  "humidity": "78%",
  "wind_speed": "5 km/h"
}
```

## 📡 Deployment
You can deploy this API using services like **Render, Railway, Fly.io, or Heroku**. 

## 🤝 Contribution
Feel free to fork this repo and submit pull requests for improvements.

## 📜 License
This project is licensed under the MIT License.

## 📞 Contact
For any inquiries, feel free to reach out via GitHub Issues.
