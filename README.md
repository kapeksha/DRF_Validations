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

Project Endpoints

    GET /projects/: Retrieve a list of all projects.
    POST /projects/: Create a new project.
    GET /projects/{id}/: Retrieve a specific project by ID.
    PUT /projects/{id}/: Update a specific project by ID.
    DELETE /projects/{id}/: Delete a specific project by ID.

Task Endpoints

    GET /tasks/: Retrieve a list of all tasks.
    POST /tasks/: Create a new task.
    GET /tasks/{id}/: Retrieve a specific task by ID.
    PUT /tasks/{id}/: Update a specific task by ID.
    DELETE /tasks/{id}/: Delete a specific task by ID.

TaskAssignment Endpoints

    GET /task-assignments/: Retrieve a list of all task assignments.
    POST /task-assignments/: Create a new task assignment.
    GET /task-assignments/{id}/: Retrieve a specific task assignment by ID.
    PUT /task-assignments/{id}/: Update a specific task assignment by ID.
    DELETE /task-assignments/{id}/: Delete a specific task assignment by ID.

Comment Endpoints

    GET /comments/: Retrieve a list of all comments.
    POST /comments/: Create a new comment.
    GET /comments/{id}/: Retrieve a specific comment by ID.
    PUT /comments/{id}/: Update a specific comment by ID.
    DELETE /comments/{id}/: Delete a specific comment by ID.

Category Endpoints

    GET /categories/: Retrieve a list of all categories.
    POST /categories/: Create a new category.
    GET /categories/{id}/: Retrieve a specific category by ID.
    PUT /categories/{id}/: Update a specific category by ID.
    DELETE /categories/{id}/: Delete a specific category by ID.

## Models

### Project

    id: AutoField (Primary Key)
    title: CharField
    description: TextField
    category: ForeignKey (Category)

### Task

    id: AutoField (Primary Key)
    title: CharField
    description: TextField
    project: ForeignKey (Project)
    due_date: DateTimeField

### TaskAssignment

    id: AutoField (Primary Key)
    task: ForeignKey (Task)
    assignee: ForeignKey (User)

### Comment

    id: AutoField (Primary Key)
    task: ForeignKey (Task)
    author: ForeignKey (User)
    content: TextField
    

## Validation

### ProjectSerializer

    validate: Ensures the title is not empty.

### TaskSerializer

    validate_due_date: Ensures the due date is not in the past.
    validate: Ensures the title is not empty.

### TaskAssignmentSerializer

    validate: Ensures the task and assignee are valid.

### CommentSerializer

    validate: Ensures the content is not empty.

    
