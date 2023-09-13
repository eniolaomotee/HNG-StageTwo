# REST API Documentation

This documentation outlines our REST API and explains the CRUD operation performed.The API is built using Python, SQLAlchemy, and SQLite and provides Create, Read, Update, and Delete (CRUD) operations.

## Table of Contents

1. [Request and Response Formats](#request-and-response-formats)
2. [Sample Usage](#sample-usage)
3. [Setting Up Locally](#setting-up-locally)
4.  [Limitations and Assumptions](#limitations-and-assumptions)

---

## Request and Response Formats

### Create a New Person

**Endpoint:** `/api` (HTTP POST):

**Request Format:**
  
  `{
  "name": "Eniola"
}`

**Response Format (Success):**

`{
    "name": "Eniola",
    "id": 1
}`
<br>

**Response:**

`201 Created` if the user is successfully created. A an JSON object containing the details of the created user is returned.

`400 Bad Request` if the request is invalid E.g The name passed is not a string, or the name is not passed at all.

`500 Internal Server Error` if there is an issue with database operations.

### Retrieve Person Details
**Endpoint:` /api/{user_id}` (HTTP GET)**

**Response Format (Success):**

`{
    "name": "John Doe",
    "id":1
}`

### Modifying Details of an Existing Person
**Endpoint: `/api/{user_id}` (HTTP PUT)**

**Request Format:**

`{
    "name": "Updated Name"
}`

**Response Format (Success):**

`{
    "name": "Updated Name",
      "id": 1,
}`

### Delete a Person
**Endpoint: `/api/{user_id}` (HTTP DELETE)**

**Response Format (Success):**

`{
    "message": "Person with ID 1 has been deleted."
}`


## Sample Usage
### Create a New Person
**Request**
```
 POST /api
Content-Type: application/json
{
    "name": "Eniola"
}
```
**Response(Success)**
```HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 1,
    "name": "Eniola"
}
```

### Retrieve Person Details
**Request**
`GET /api/1 `

**Response(Success)**
```HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "name": "Eniola",
}
```
### Update Person Details
**Request**
```PUT /api/1
Content-Type: application/json

{
    "name": "Updated Name",
}
```
**Response(Success)**
```HTTP/1.1 200 OK
Content-Type: application/json
{
    "id": 1,
    "name": "Updated Name",
}
```
### Delete a Person
**Request**
`DELETE /api/1`

**Response(Success)**
```
HTTP/1.1 200 OK
Content-Type: application/json
{
    "message": "Person with ID 1 has been deleted."
}
```


## Setting Up Locally
* Clone the repository from Github.
* Navigate to the project directory in your computer and open it with your code editor.
* Install the required dependencies using pip install -r requirements.txt.
* Start the API with `uvicorn app.main:app --host localhost --port 8000 --reload `.
* You can view it on swagger UI on `/docs`
  
## Limitations and Assumptions
* The API assumes that the database schema is already set up correctly.
* Authorization mechanisms are not covered but should be added for security in a real-world scenario.
