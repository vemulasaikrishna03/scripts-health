import requests

def check_uwsgi_health():
    try:
        response = requests.get('http://localhost:5000')
        if response.status_code == 200:
            print("healthy")
        else:
            print(f"uwsgi is unhealthy. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error checking uwsgi health: {e}")

check_uwsgi_health()
