
# Student Grades Management System

This is a console-based system built in Python that uses SQLite to manage student records and their grades.

## Features

- Add new students to the database
- View all student information including grades and average
- Modify student details
- Delete students and their grades
- Add grades for registered students
- Display students and their average scores

## Technologies Used

- Python 3
- SQLite (via sqlite3 module)
- Local file storage for database

## Database Structure

The SQLite database contains two tables:

### Table: `alumnos` (Students)

| Column             | Type    | Description                       |
|--------------------|---------|-----------------------------------|
| ID_alumno          | INTEGER | Primary Key, auto-increment       |
| Nombre_alumno      | TEXT    | First name of the student         |
| Apellido_alumno    | TEXT    | Last name of the student          |
| Fecha_nacimiento   | DATE    | Birth date                        |
| Carrera            | TEXT    | Degree or major                   |
| Direccion          | TEXT    | Address                           |

### Table: `notas` (Grades)

| Column      | Type    | Description                                  |
|-------------|---------|----------------------------------------------|
| ID_nota     | INTEGER | Primary Key, auto-increment                  |
| ID_alumno   | INTEGER | Foreign key referencing `alumnos` table      |
| Clase       | TEXT    | Subject or course name                       |
| Nota1       | REAL    | First grade                                  |
| Nota2       | REAL    | Second grade                                 |
| Nota3       | REAL    | Third grade                                  |

## How to Use

1. Run the script with a Python interpreter.
2. Choose one of the menu options:
    - Add student
    - View student list
    - Modify student details
    - Delete a student
    - Add grades
    - View detailed student information and grades
    - Exit the program

## Notes

- The database is stored at:
  `C:/Users/aleja/Desktop/III Semestre 2024/Base da datos relacionales/repaso_9_12_24/examen/bddregistronotas.db`

- The system ensures tables are created if they do not exist.

- Grade averages are automatically calculated when viewing student details.

## Author

Developed as part of a coursework project for a database systems class.
