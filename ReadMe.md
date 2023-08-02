# Project Name

## Description

This project, "Project Name," is a web application developed using Django, a high-level Python web framework. It aims to provide a user-friendly interface for managing a pizza restaurant's menu, allowing users to create, update, and delete pizza items with various toppings and crust types.

## Features

- **Pizza Management**: Users can create new pizza items with custom toppings, sauces, and crust types, providing flexibility in creating diverse pizza combinations.

- **Dough Types**: The application supports various dough types, such as "Средна," "Голяма," and "Джъмбо," with their respective descriptions and prices.

- **Ingredients**: Users can add and manage a wide range of ingredients like spices, meats, vegetables, cheese, and sauces that can be used in pizza recipes.

- **Tags**: The system allows users to tag pizza items with descriptive tags, making it easier for customers to filter and find their preferred pizza choices.

- **Image Uploads**: The application supports image uploads for pizza items, ingredients, and tags, making the menu visually appealing.

- **Database Backup**: A script is provided to create backups of the database in JSON format, facilitating easy data preservation.

## Database Diagram

Below is the Entity-Relationship Diagram (ERD) representing the main models used in the database:

![Database Diagram](link-to-image)

## Setup and Usage

1. Clone the repository and navigate to the project directory.

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Apply the database migrations:

   ```
   python manage.py migrate
   ```

5. Create an admin superuser:

   ```
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```
   python manage.py runserver
   ```

7. Access the admin panel at http://localhost:8000/admin/ and use the superuser credentials to log in.

8. Begin managing the pizza menu and ingredients via the admin panel.

## Contribution

Contributions to the project are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](link-to-license-file) file for details.