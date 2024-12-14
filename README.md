# Quiz App

A simple Django-based quiz application that allows users to answer multiple-choice questions and track their performance.

## Features

- Start a new quiz session
- Answer multiple-choice questions
- View results with correct and incorrect answers
- Admin interface for managing questions

## Prerequisites

- Python 3.x
- Django
- pip (Python package installer)

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   cd quiz-app
   ```

2. **Create a Virtual Environment**
   It’s recommended to create a virtual environment to manage dependencies.
   ```bash
   python -m venv env
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**
   Install the required packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Database**
   Run the following commands to create the database and apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Populate Questions (Optional)**
   If you have a JSON file with questions, you can populate the database using the management command:
   ```bash
   python manage.py populate_questions path/to/your/questions.json
   ```

7. **Run the Development Server**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000/` to access the quiz application.

## Usage

- Click on "Start Quiz" to begin.
- Answer the questions and submit your answers.
- View your results at the end of the quiz.

## Admin Interface

To manage questions, you can access the Django admin interface at `http://127.0.0.1:8000/admin/`. You will need to create a superuser to log in:
```bash
python manage.py createsuperuser
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Django documentation for guidance on setting up the project.
- Inspiration from various online quiz applications.