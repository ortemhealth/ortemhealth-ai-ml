import requests

def test_predict():
    sample = {
        "age": 38,
        "past_no_shows": 1,
        "weekday": 2,
        "lead_days": 4,
        "has_reminder": 1
    }
    response = requests.post("http://localhost:7000/no-show/predict", json=sample)
    assert response.status_code == 200
    out = response.json()
    print(out)
    assert 0 <= out["no_show_probability"] <= 1

if __name__ == "__main__":
    test_predict()
