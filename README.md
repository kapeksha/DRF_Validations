# Task Management API

This is a RESTful API for managing tasks, their statuses, and categories. The API is built with Django and Django REST Framework.

## Setup

1. **Clone the repository:**
  ```sh
  git clone https://github.com/yourusername/task-management-api.git
  cd task-management-api
  ```

2. **Create a virtual environment and activate it:**
```sh
  python3 -m venv env
  source env/bin/activate
  ```

3. **Run the database migrations:**
  ```sh
  python3 manage.py migrate
  ```

4. **Start the development server:**
    ```sh
   python3 manage.py runserver
    ```
## Usage

Once the server is running, you can interact with the API using a tool like curl, Postman, or your web browser.

## API Endpoints

### Task Endpoints
    GET /tasks/: Retrieve a list of all tasks.
    POST /tasks/: Create a new task.
    GET /tasks/{id}/: Retrieve a specific task by ID.
    PUT /tasks/{id}/: Update a specific task by ID.
    DELETE /tasks/{id}/: Delete a specific task by ID.

### Status Endpoints

    GET /statuses/: Retrieve a list of all statuses.
    POST /statuses/: Create a new status.
    GET /statuses/{id}/: Retrieve a specific status by ID.
    PUT /statuses/{id}/: Update a specific status by ID.
    DELETE /statuses/{id}/: Delete a specific status by ID.

### Category Endpoints

    GET /categories/: Retrieve a list of all categories.
    POST /categories/: Create a new category.
    GET /categories/{id}/: Retrieve a specific category by ID.
    PUT /categories/{id}/: Update a specific category by ID.
    DELETE /categories/{id}/: Delete a specific category by ID.


## Models

## Task

    id: AutoField (Primary Key)
    title: CharField
    description: TextField
    status: ForeignKey (Status)
    category: ForeignKey (Category)
    due_date: DateTimeField

### Status

    id: AutoField (Primary Key)
    name: CharField (Choices: 'To-Do', 'In Progress', 'Complete')

### Category

    id: AutoField (Primary Key)
    name: CharField

## Validation

### TaskSerializer

    validate_due_date: Ensures the due date is not in the past.
    validate: Ensures the title is not empty.

### StatusSerializer

    validate_name: Ensures the status name is one of the valid choices ('To-Do', 'In Progress', 'Complete').

### CategorySerializer

    validate_name: Ensures the category name is not empty.
    
