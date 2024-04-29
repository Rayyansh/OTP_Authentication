# Django OTP Authentication

Welcome to the Django OTP Authentication project! This repository provides a guide and code for setting up OTP authentication in your Django and Django REST Framework application. Follow the steps below to set up and run the code.

## Requirements

Before you get started, make sure you have the following installed:

- Python 3
- Django
- Django REST Framework
- Other required packages specified in `requirements.txt`

## Setup

1. **Clone the repository**: Start by cloning this repository to your local machine.

    ```bash
    git clone <repository_url>
    ```

2. **Navigate to the project directory**: Change into the project directory.

    ```bash
    cd <project_directory>
    ```

3. **Create a virtual environment**: This step is optional but recommended for isolating your project's dependencies.

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment**: Depending on your operating system, use the following commands to activate the virtual environment:

    - **On Windows**:

        ```bash
        venv\Scripts\activate
        ```

    - **On macOS/Linux**:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies**: Install the required packages using `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

6. **Configure your settings**: Make sure to update `settings.py` with the appropriate configurations for your project, including the SMS API key and other necessary settings.

7. **Set up the database**: Create the OTP model and apply migrations to set up the database.

    - **Create migrations**:

        ```bash
        python manage.py makemigrations
        ```

    - **Apply migrations**:

        ```bash
        python manage.py migrate
        ```

8. **Run the development server**: Start the Django development server to test the application.

    ```bash
    python manage.py runserver
    ```

That's it! You should now have the OTP authentication set up and running in your Django application.

## Code Overview

- `models.py`: Defines the OTP model for storing OTPs and associated information.
- `views.py`: Contains `LoginView` and `VerifyOTPView` to handle user login and OTP verification.
- `urls.py`: Defines URL routes for the application.

## Additional Notes

- Make sure to customize the code according to your project's requirements.
- For production use, consider enhancing security and performance.
- Review the code and configurations for potential improvements or optimizations.

## Contributing

Feel free to contribute to this project! You can submit pull requests or open issues with suggestions for improvements.
