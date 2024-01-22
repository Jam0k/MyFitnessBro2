from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Food(db.Model):
    __tablename__ = 'foods'

    food_id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(255), nullable=False)
    food_serving_size = db.Column(db.String(255))
    food_calories = db.Column(db.Numeric(10, 2))
    food_protein = db.Column(db.Numeric(10, 2))
    food_fat = db.Column(db.Numeric(10, 2))
    food_carbohydrate = db.Column(db.Numeric(10, 2))
    food_sugar = db.Column(db.Numeric(10, 2))

class Meal(db.Model):
    __tablename__ = 'meals'

    meal_id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(255), nullable=False)

class MealFoods(db.Model):
    __tablename__ = 'meal_foods'

    meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'), primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'), primary_key=True)
    food_serving_size = db.Column(db.String(255))

class NutritionLog(db.Model):
    __tablename__ = 'nutrition_logs'

    log_id = db.Column(db.Integer, primary_key=True)
    mealtime = db.Column(db.String(255))
    food_id = db.Column(db.Integer, db.ForeignKey('foods.food_id'), nullable=True)
    serving_size = db.Column(db.String(255))
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.meal_id'), nullable=True)
    log_date = db.Column(db.Date)
