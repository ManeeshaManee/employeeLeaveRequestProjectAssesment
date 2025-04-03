# Employee Leave API

This is a RESTful API for managing employee leave requests. The API allows users to create leave requests, retrieve leave requests by employee, and ensure that business rules around leave requests (such as validation of dates, overlapping leaves, and maximum consecutive leave days) are enforced.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.8+
- FastAPI
- SQLAlchemy
- SQLite
- pytest

You can install all dependencies by running:

```bash
pip install -r requirements.txt
```

### Requirements for Running the App

- **FastAPI** for building the RESTful API.
- **SQLAlchemy** for database interaction and ORM (using SQLite).
- **pytest** for testing the API and business logic.

## Setup Instructions

1. **Install dependencies:**

   Create a virtual environment and install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI application:**

   To run the FastAPI app with hot reloading, use the following command:

   ```bash
   uvicorn app.main:app --reload
   ```

   By default, the API will be available at `http://127.0.0.1:8000`.

3. **Access the API Documentation:**

   FastAPI automatically generates API documentation for you. To access the interactive docs, navigate to:

   ```
   http://127.0.0.1:8000/docs
   ```

   Or, for the alternative Swagger UI, go to:

   ```
   http://127.0.0.1:8000/redoc
   ```

## API Endpoints

### POST `/api/v1/leave-requests`

Create a new leave request.

#### Request Body:

```json
{
  "employee_id": "EMP001",
  "start_date": "2025-03-01",
  "end_date": "2025-03-05",
  "leave_type": "ANNUAL",
  "reason": "Family vacation to visit parents"
}
```

#### Response:

```json
{
  "id": "LR001",
  "employee_id": "EMP001",
  "start_date": "2025-03-01",
  "end_date": "2025-03-05",
  "leave_type": "ANNUAL",
  "reason": "Family vacation to visit parents",
  "status": "PENDING",
  "working_days": 3,
  "created_at": "2025-02-11T10:00:00Z"
}
```

#### Validation:

- `end_date` must be after `start_date`.
- The employee cannot have overlapping leave requests.
- Maximum consecutive leave days: 14.

### GET `/api/v1/leave-requests/{employee_id}`

Get all leave requests for a specific employee.

#### Example Request:

```
GET /api/v1/leave-requests/EMP001
```

#### Response:

```json
[
  {
    "id": "LR001",
    "employee_id": "EMP001",
    "start_date": "2025-03-01",
    "end_date": "2025-03-05",
    "leave_type": "ANNUAL",
    "reason": "Family vacation",
    "status": "PENDING",
    "working_days": 3,
    "created_at": "2025-02-11T10:00:00Z"
  }
]
```

### Error Response (Validation Errors)

In case of invalid data, the API will respond with the following error structure:

```json
{
  "error": "VALIDATION_ERROR",
  "message": "Invalid request",
  "details": [
    "end_date must be after start_date",
    "maximum consecutive leave days is 14"
  ]
}
```

## Running Tests

To ensure that the API and business logic work correctly, unit tests are included in the `tests/` directory. You can run them using `pytest`:

1. Install pytest if it's not already installed:

   ```bash
   pip install pytest
   ```

2. Run the tests:

   ```bash
   pytest
   ```

   This will automatically discover and run all tests in the `tests/` folder.

### Example Test:

Here's a basic test for creating a leave request:

```python
def test_create_leave_request():
    response = client.post("/api/v1/leave-requests", json={
        "employee_id": "EMP001",
        "start_date": "2025-03-01",
        "end_date": "2025-03-05",
        "leave_type": "ANNUAL",
        "reason": "Family vacation to visit parents"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["employee_id"] == "EMP001"
```

