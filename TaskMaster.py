import requests
import pytest

base_url = 'http://127.0.0.1:5000/tasks'
headers = {
    'Content-Type': 'application/json'
}
###POST###
@pytest.mark.parametrize('task_data',[                   #@pytest.mark.parametrize - for running multiple test cases
    { 
        "title": "Complete API Testing Practice",        #valid json values, excpected status code 200
        "description": "write test cases",
        "due_date": "2024-06-18"
    },
    {
        "description": "write test cases",               #missing json fields, excpected status code 404
        "due_date": "2024-06-18"
    },
    {
        "title": "Complete API Testing Practice",
        "description": "write test cases",               #additioal json fields, excpected code 200  (assuming the api ignoring the extra fields)
        "due_date": "2024-06-18",
        "hour": "1 pm",
    },
    {
        "title": "Complete API Testing Practice",
        "description": "write test cases",               #invalid date format, excpected status code 404
        "due_date": "May",
    },
    {
        "title": "Jonathan Coe's novel, 'The Rotters' Club', contains a sentence of 13,955 words. This is generally considered to be the longest sentence in English literature.",
        "description": "write test cases",               # assume there is a char limit: check if title length is less than 50 chars, if len < 50 status code 200, else status code 400
        "due_date": "2024-06-18",
    },
    {
        "title": "Complete API Testing Practice",
        "description": "write test cases",               # assume that null value is not alowed, excpected status code 404
        "due_date": null,
    },

])

def test_create_task(task_data):
    response = requests.post(base_url, headers=headers, json=task_data)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}" #check what is the actual status code

###PUT###
@pytest.mark.parametrize('task_id',[1,300,'A']) # assuming id 1 exists, expected status code 200.
                                                # assuming id 300 doesn't exists, expected status code 404.
                                                # assuming id A is not valid (id is numeric), expected status code 404.
def test_update_task(task_data, task_id):
    url = f'{base_url}/{task_id}'
    response = requests.put(url, headers=headers, json=task_data)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

###Get###
def test_get_task(task_id):
    url = f'{base_url}/{task_id}'
    response = requests.get(url, headers=headers)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
