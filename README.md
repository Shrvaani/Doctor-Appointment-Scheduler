# Doctor Appointment System

A simple Django-based web application for booking and managing doctor appointments.

## Features

- User Registration
- User Login/Logout
- Book Appointments
- View Appointment Schedule

## Installation

### Prerequisites

- Python 3.11
- Django 5.0.6

### Setup

1. Clone the repository:
    ```bash
    git clone [https://github.com/Shrvaani/Doctor-Appointment-Scheduler.git]
    cd doctor-appointment-system
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

- Navigate to `/register/` to create a new account.
- Navigate to `/login/` to log in.
- Once logged in, you can book an appointment and view your appointments.

## Project Structure

- `appointments/`: Contains the main app for handling appointments and user interactions.
- `doctor_appointment_project/`: Contains project settings and configurations.
- `templates/`: Contains HTML templates for rendering views.

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any changes or suggestions.

## License

This project is licensed under the MIT License.
