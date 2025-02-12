# Weather API - Real-time Weather Information with Email and Telegram Notifications

## About the Project
This project provides real-time weather information using Django and Django REST Framework. Users can receive weather updates via email and Telegram bot notifications. The system integrates OpenWeather API for fetching weather data and uses Redis for caching to enhance performance.

## Features
- **Real-time Weather API**: Get weather details for any city using a RESTful API.
- **Email Notifications**: Users can subscribe to receive periodic weather updates via email.
- **Telegram Bot Integration**: Users can request weather updates directly from a Telegram bot.
- **Caching with Redis**: Weather data is cached to improve performance and reduce API calls.
- **Admin Panel**: Manage users, subscriptions, and notifications through the Django admin panel.
- **CRON Jobs with Celery**: Automates email notifications at scheduled intervals.

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Caching**: Redis
- **Task Scheduling**: Celery, Celery Beat
- **APIs**: OpenWeather API, Telegram Bot API
- **Deployment**: Docker, Gunicorn, Nginx

## Installation Guide
### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- PostgreSQL
- Redis
- Docker (optional for deployment)

### Setup Steps
1. **Clone the repository:**
   ```sh
   git clone https://github.com/ASILBEKasilbek/Weather-API.git
   cd Weather-API
   ```
2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure `.env` file:** (Create a `.env` file in the root directory and add the following)
   ```ini
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=*
   WEATHER_API_KEY=your_openweather_api_key
   EMAIL_HOST=smtp.your-email-provider.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-email-password
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```
5. **Run migrations:**
   ```sh
   python manage.py migrate
   ```
6. **Create a superuser (for admin panel access):**
   ```sh
   python manage.py createsuperuser
   ```
7. **Start the Django development server:**
   ```sh
   python manage.py runserver
   ```
8. **Run Celery and Redis:**
   Open a new terminal and start Redis:
   ```sh
   redis-server
   ```
   Then, start Celery worker:
   ```sh
   celery -A core worker --loglevel=info
   ```
   And start Celery Beat for periodic tasks:
   ```sh
   celery -A core beat --loglevel=info
   ```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/weather/<city>/` | GET | Get weather details for a specific city |
| `/api/subscribe/` | POST | Subscribe to email notifications |
| `/api/unsubscribe/` | POST | Unsubscribe from email notifications |

### Example API Request
```sh
curl -X GET http://127.0.0.1:8000/api/weather/London/
```

## Telegram Bot Usage
1. **Start the bot**
2. Send the command:
   ```
   /weather <city>
   ```
   Example:
   ```
   /weather New York
   ```
   The bot will respond with the current weather data.

## Deployment with Docker
1. **Build the Docker image:**
   ```sh
   docker-compose build
   ```
2. **Run the container:**
   ```sh
   docker-compose up -d
   ```

## Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact:
- **Developer:** Asilbek
- **Email:** your-email@example.com
- **GitHub:** [ASILBEKasilbek](https://github.com/ASILBEKasilbek)

