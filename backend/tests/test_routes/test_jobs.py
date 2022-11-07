import json


def test_create_job(client):
    data = {
        "title": "Middle+",
        "company": "twister",
        "company_url": "www.twister.com",
        "location": "Italy,Milan",
        "description": "Python Developer",
        "date_posted": "2022-11-03",
    }
    response = client.post("/jobs/create-job/", json.dumps(data))
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
