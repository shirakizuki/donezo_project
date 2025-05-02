# Donezo

![Donezo Logo](project/static/image/donezo_logo.png)

Donezo is a modern, user-friendly to-do management web application built with Django. It helps you organize your tasks efficiently with a clean and intuitive interface. Whether you're managing personal tasks or team projects, Donezo provides a seamless experience for tracking and completing your to-dos.

## Features

- **User Authentication**: Secure registration and login system
- **Task Management**: Create, organize, and track tasks with ease
- **Custom Priorities**: Create up to 5 custom priority levels to manage tasks
- **Labels**: Categorize tasks with custom labels for better organization
- **Dashboard Views**: Today, Upcoming, and Filter views for task management
- **Modern UI**: Clean, responsive design using Tailwind CSS
- **User Profiles**: Personal profile management

## Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (default), compatible with PostgreSQL for production
- **Authentication**: Django built-in authentication system

## Installation

### Prerequisites
- Python 3.8 or higher
- Node.js and npm (for Tailwind CSS)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shirazaki/donezo.git
   cd donezo
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Node.js dependencies:
   ```bash
   npm install
   ```

5. Run database migrations:
   ```bash
   cd project
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. In a separate terminal, start the Tailwind CSS watcher:
   ```bash
   npm run watch:css
   ```

The application should now be running at `http://127.0.0.1:8000/`

## Project Structure

```
donezo_project/
├── LICENSE                  # MIT License
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies and scripts
├── project/                # Django project directory
│   ├── db.sqlite3          # SQLite database
│   ├── manage.py           # Django management script
│   ├── app/                # Main application
│   │   ├── models.py       # Data models (Priority, Label)
│   │   ├── views.py        # View controllers
│   │   ├── forms.py        # Form definitions
│   │   ├── urls.py         # URL routing
│   │   └── templates/      # HTML templates
│   ├── project/            # Django settings module
│   │   ├── settings.py     # Project settings
│   │   ├── urls.py         # Root URL configuration
│   │   └── wsgi.py         # WSGI configuration
│   ├── static/             # Static files
│   │   ├── image/          # Images and icons
│   │   ├── js/             # JavaScript files
│   │   └── src/            # Source styles for Tailwind CSS
│   └── templates/          # Base templates
```

## Usage

1. Register a new account or login with existing credentials.
2. Once logged in, you'll be directed to your dashboard.
3. Use the sidebar to navigate between different views:
   - **Today**: Manage tasks due today
   - **Upcoming**: View and organize future tasks
   - **Filter & Links**: Create and manage priorities and labels
   - **Profile**: View your user profile

### Filter & Links Feature

The Filter & Links section helps you organize your tasks with custom priorities and labels:

#### Managing Priorities

Priorities help you rank your tasks by importance. You can:
- Create up to 5 custom priorities
- Name them according to your workflow (e.g., "Urgent", "High", "Medium", "Low", "Optional")
- Edit existing priorities by clicking the edit (pencil) icon
- Delete priorities you no longer need with the delete (trash) icon

**Note**: Each user can have a maximum of 5 priorities. You'll need to delete an existing one before adding a new one if you've reached the limit.

#### Working with Labels

Labels help categorize your tasks by project, context, or any other organizational system you prefer:
- Create unlimited custom labels
- Group related tasks under meaningful categories (e.g., "Work", "Personal", "Health", "Learning")
- Edit labels to refine your organizational system
- Delete labels that are no longer relevant

#### Best Practices

- Create a consistent priority system that makes sense for your workflow
- Use descriptive names for your labels to quickly identify task categories
- Regularly review and refine your priorities and labels as your needs change
- Consider using color-coding in your mind: high priorities for tasks that must be done today, medium for this week, and low for eventual completion

## Development

### Commands

- Run tests: `python manage.py test`
- Create a superuser: `python manage.py createsuperuser`
- Build CSS for production: `npm run build:css`

### Adding Features
To add new features or modify existing ones, work with the following files:
- Models: `project/app/models.py`
- Views: `project/app/views.py`
- Templates: `project/app/templates/`
- URLs: `project/app/urls.py`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
