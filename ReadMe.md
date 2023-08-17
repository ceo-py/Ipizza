# Ipizza

# Website Deployment

This repository outlines the seamless deployment of a dynamic website using a custom domain name, a customized Linux VPS setup, Apache2 configuration with an SSL certificate, and the fine-tuning of Apache2 and Django for optimal performance.

## Key Features

- **Custom Domain:** Utilize a personalized domain name.
- **Custom Linux VPS:** Set up a tailored Linux Virtual Private Server (VPS) for hosting.
- **Apache2 Configuration:** Configure the Apache2 web server.
- **SSL Security:** Ensure data security with an SSL certificate.
- **Apache2 and Django Integration:** Fine-tune the interaction between Apache2 and Django for seamless functionality.

## Explore the Site

You can visit the deployed site and experience its features firsthand by clicking [here](https://ipizza.ceo-py.eu/).

## Description

The project is a web application for a pizza restaurant that offers a diverse menu, including pizza, drinks, sandwiches, salads, pasta, and more. Users can customize their orders by adding or removing toppings from the items in the menu. They can add desired items to the cart and proceed to make payments for their order. The application aims to provide a user-friendly interface for managing orders and enhancing the overall dining experience.
Deployment

## Features

The application provides the following features:

- **Menu Variety**: The restaurant offers a diverse menu, including pizza, drinks, sandwiches, salads, pasta, and other delicious items, catering to different tastes and preferences.

- **Customization**: Users can easily customize their orders by adding or removing toppings from the available items in the menu, allowing them to create personalized dishes.

- **Shopping Cart**: Customers can add multiple items to their cart and review their selections before proceeding to checkout.

- **User Accounts**: Users can create accounts and log in to access additional features, such as order history and personalized preferences.

- **Admin Panel**: The application provides an admin panel for restaurant staff to manage the menu, process orders, and view sales data.

- **Responsive Design**: The web application is built with a responsive design, ensuring a seamless experience across various devices, including desktops, tablets, and mobile phones.


Overall, the project aims to enhance the restaurant's efficiency and customer satisfaction by offering a convenient and user-friendly platform for ordering food and beverages.
## Database Diagram

Below is the Entity-Relationship Diagram (ERD) representing the main models used in the database:

![Database Diagram](https://github.com/ceo-py/Ipizza/blob/master/DB_DIAGRAM.png)

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
   python manage.py makemigrations
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

7. Populate DataBase:

   ```
   python manage.py loaddata output_fileB.json
   ```

8. Access the admin panel at http://localhost:8000/admin/ and use the superuser credentials to log in.

9. Begin managing the pizza menu and ingredients via the admin panel or web.
