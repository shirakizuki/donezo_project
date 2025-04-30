# donezo_project
Personal to do management web base application using django.

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for Tailwind CSS)

### Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Tailwind CSS:
   ```bash
   # Install Tailwind CSS CLI
   npm install -D tailwindcss

   # Initialize Tailwind CSS
   npx tailwindcss init
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. In a separate terminal, start the Tailwind CSS watcher:
   ```bash
   npx tailwindcss -i ./static/src/input.css -o ./static/dist/output.css --watch
   ```

The application should now be running at `http://127.0.0.1:8000/`
