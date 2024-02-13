# Vending machine

## a crm app for a vending machine

## Requirements

- Python (version 3.10)
- Django (version 5.0.2)

## Installation

1. Clone the repository:

    ```
    git clone git@github.com:AbdallahMGomaa/vendingmachine.git
    ```

2. Create a virtual environment

    ```
    virtualenv venv
    ```
3. activate virtual environment
    ```
    source venv/bin/activate
    ```

4. Navigate to the project directory:

    ```
    cd vendingmachine
    ```

5. Install dependencies:

    ```
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```
    ./manage.py migrate
    ```

## Running the Application

1. Start the development server:

    ```
    python manage.py runserver 0.0.0.0:8000
    ```

2. Open a web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to view the application.
