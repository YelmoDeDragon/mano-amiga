import requests


def get_students():
    url = "http://127.0.0.1:8000/api/students/"
    response = requests.get(url)

    if response.status_code == 200:
        students = response.json()
        print("List of Students:")
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Lastname: {student['lastname']}")
    else:
        print(f"Failed to retrieve students. Status code: {response.status_code}")


if __name__ == "__main__":
    get_students()
