from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os
import logging

# Import models here
from models import db, Food, Meal, MealFoods, NutritionLog

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Initialize the database with the app
db.init_app(app)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check database connection
def check_db_connection():
    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1"))
            for _ in result:
                logger.info("Database connection test passed.")
            logger.info("Connected to the database successfully.")
        except SQLAlchemyError as e:
            logger.error(f"Database connection failed: {e}")

check_db_connection()

@app.route('/')
def dashboard():
    logger.info("Dashboard accessed")  # Log when the dashboard is accessed
    return render_template('dashboard.html')

@app.route('/nutrition_logs')
def get_nutrition_logs():
    try:
        # Query the database for nutrition logs
        logs = NutritionLog.query.all()
        log_list = []

        for log in logs:
            # Fetch related food and meal details, if present
            food = Food.query.get(log.food_id)
            meal = Meal.query.get(log.meal_id)

            log_entry = {
                'log_id': log.log_id,
                'log_date': log.log_date.isoformat(),
                'mealtime': log.mealtime,
                'food': food.food_name if food else None,
                'meal': meal.meal_name if meal else None
            }
            log_list.append(log_entry)

        return jsonify(log_list)
    except SQLAlchemyError as e:
        logger.error(f"Failed to fetch nutrition logs: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500

# Error handlers

@app.errorhandler(404)
def page_not_found(e):
    logger.error(f'Page not found: {e}')  # Log the error
    return render_template('error.html', error_message='Page not found', status_code=404), 404

@app.errorhandler(500)
def internal_server_error(e):
    logger.error(f'Internal server error: {e}')  # Log the error
    return render_template('error.html', error_message='Internal server error', status_code=500), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
