import requests


def add_student(student_data):
    url = "http://127.0.0.1:8000/api/students/"
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=student_data, headers=headers)

    if response.status_code in (200, 201):  # HTTP 201 Created
        print("Student added successfully:", response.json())
    else:
        print(f"Failed to add student. Status code: {response.status_code}, Error: {response.text}")


if __name__ == "__main__":
    new_student = {
        "name": "John",
        "lastname": "Doe",
        "address": "123 Main St",
        "email": "john.doe@example.com",
        "school": "XYZ University"
    }
    add_student(new_student)
