CREATE TABLE foods (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255) NOT NULL,
    food_serving_size VARCHAR(255),
    food_calories DECIMAL(10,2),
    food_protein DECIMAL(10,2),
    food_fat DECIMAL(10,2),
    food_carbohydrate DECIMAL(10,2),
    food_sugar DECIMAL(10,2)
);

CREATE TABLE meals (
    meal_id SERIAL PRIMARY KEY,
    meal_name VARCHAR(255) NOT NULL
);

CREATE TABLE meal_foods (
    meal_id INT,
    food_id INT,
    food_serving_size VARCHAR(255),
    PRIMARY KEY (meal_id, food_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id),
    FOREIGN KEY (food_id) REFERENCES foods(food_id)
);


CREATE TABLE nutrition_logs (
    log_id SERIAL PRIMARY KEY,
    mealtime VARCHAR(255),
    food_id INT,
    meal_id INT,
    log_date DATE,
    FOREIGN KEY (food_id) REFERENCES foods(food_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);
