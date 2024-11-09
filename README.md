# Project Name: Flask Database Management System

This is a Flask-based web application for managing database projects. The app allows users to create projects, define tables within those projects, and add fields to each table. This project serves as a basic framework for managing relational databases with a clean interface and the flexibility to extend and modify as needed.

## Features

- **User Management**: Users can create an account and manage their profile.
- **Project Management**: Users can create, update, and delete projects.
- **Table Management**: Each project can have multiple tables, and users can define tables with custom names and descriptions.
- **Field Management**: Users can define fields for each table with specified data types.

## Technologies Used

| Technology    | Description                                                      |
|---------------|------------------------------------------------------------------|
| **Python 3.8+** | Programming language used for the backend.                      |
| **Flask**      | A lightweight WSGI web application framework.                    |
| **SQLAlchemy** | ORM for database operations.                                    |
| **SQLite**     | Default database for development and testing.                   |
| **Flask-Migrate** | For database migration handling.                              |
| **Enum**       | To define user types and roles.                                  |

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hasnaat-iftikhar/DB-Visualizer-API.git
   cd repository-name
   ```

2. Set up your virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your database and migration:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:

   ```bash
   flask run
   ```

   The app will be available at `http://127.0.0.1:5000/`.

## API Endpoints

| HTTP Method | Endpoint             | Description                                             |
|-------------|----------------------|---------------------------------------------------------|
| **GET**     | /api/users           | Get the list of all users.                              |
| **POST**    | /api/users           | Create a new user.                                      |
| **GET**     | /api/projects        | Get the list of all projects for a user.                |
| **POST**    | /api/projects        | Create a new project.                                   |
| **GET**     | /api/tables          | Get the list of all tables for a project.               |
| **POST**    | /api/tables          | Create a new table in a project.                        |
| **GET**     | /api/fields          | Get the list of all fields for a table.                 |
| **POST**    | /api/fields          | Create a new field in a table.                          |

## Database Models

### User Model

| Column Name    | Data Type         | Description                                         |
|----------------|-------------------|-----------------------------------------------------|
| **id**         | Integer (Primary Key) | Unique identifier for each user.                  |
| **username**   | String            | Unique username for each user.                     |
| **first_name** | String            | User's first name.                                  |
| **last_name**  | String            | User's last name.                                   |
| **email**      | String            | User's email address.                               |
| **password**   | String            | User's hashed password.                             |
| **profile_picture** | String      | URL/path to the user's profile picture.            |
| **user_type**  | Enum (UserTypeEnum) | Type of the user (student or professional).       |
| **role**       | Enum (RoleEnum)    | Role of the user (developer, database designer).    |
| **company_name** | String (Optional) | User's company name (if applicable).              |
| **created_at** | DateTime          | Timestamp when the user was created.                |
| **updated_at** | DateTime          | Timestamp when the user was last updated.           |

### Project Model

| Column Name    | Data Type         | Description                                         |
|----------------|-------------------|-----------------------------------------------------|
| **id**         | Integer (Primary Key) | Unique identifier for each project.              |
| **user_id**    | Integer (Foreign Key) | User who created the project.                     |
| **name**       | String            | Name of the project.                                |
| **description**| String (Optional) | Description of the project.                         |
| **created_at** | DateTime          | Timestamp when the project was created.             |
| **updated_at** | DateTime          | Timestamp when the project was last updated.        |

### Table Model

| Column Name    | Data Type         | Description                                         |
|----------------|-------------------|-----------------------------------------------------|
| **id**         | Integer (Primary Key) | Unique identifier for each table.                 |
| **project_id** | Integer (Foreign Key) | Project to which the table belongs.               |
| **name**       | String            | Name of the table.                                  |
| **created_at** | DateTime          | Timestamp when the table was created.               |
| **updated_at** | DateTime          | Timestamp when the table was last updated.          |

### Field Model

| Column Name    | Data Type         | Description                                         |
|----------------|-------------------|-----------------------------------------------------|
| **id**         | Integer (Primary Key) | Unique identifier for each field.                 |
| **table_id**   | Integer (Foreign Key) | Table to which the field belongs.                 |
| **name**       | String            | Name of the field.                                  |
| **type**       | String            | Data type of the field (e.g., string, integer).    |
| **created_at** | DateTime          | Timestamp when the field was created.               |
| **updated_at** | DateTime          | Timestamp when the field was last updated.          |

## Contributing

We welcome contributions to this project. Here are some ways you can help:

1. **Fork the repository** and create your branch.
2. **Submit issues** if you find any bugs or have feature requests.
3. **Create pull requests** to propose new features or fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.