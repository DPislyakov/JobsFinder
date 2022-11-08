import json

from fastapi import status


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "Middle+",
        "company": "twister",
        "company_url": "www.twister.com",
        "location": "Italy,Milan",
        "description": "Python Developer",
        "date_posted": "2022-11-03",
    }
    response = client.post(
        "/jobs/create-job/", data=json.dumps(data), headers=normal_user_token_headers
    )
    assert response.status_code == 200
    assert response.json()["company"] == "twister"
    assert response.json()["title"] == "Middle+"


def test_read_job(client):
    data = {
        "title": "Middle+",
        "company": "twister",
        "company_url": "www.twister.com",
        "location": "Italy,Milan",
        "description": "Python Developer",
        "date_posted": "2022-11-03",
    }
    response = client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("jobs/get/1/")
    assert response.status_code == 200
    assert response.json()["description"] == "Python Developer"


def test_read_all_jobs(client):
    data = {
        "title": "Senior Backender",
        "company": "MS",
        "company_url": "www.ms.com",
        "location": "USA,California",
        "description": "Go",
        "date_posted": "2022-10-21",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/all/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "Senior Backender",
        "company": "MS",
        "company_url": "www.ms.com",
        "location": "USA,California",
        "description": "Go",
        "date_posted": "2022-10-21",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/jobs/update/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_a_job(client):
    data = {
        "title": "Senior Backender",
        "company": "MS",
        "company_url": "www.ms.com",
        "location": "USA,California",
        "description": "Go",
        "date_posted": "2022-10-21",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    client.delete("/jobs/delete/1")
    response = client.get("/jobs/get/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
