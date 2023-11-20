from celery import Celery
from celery.result import AsyncResult

app = Celery('NSpace')

def check_celery_beat_health():
    try:
        result = AsyncResult('beat_schedule', app=app)

        if result.state == 'STARTED':
            print("Celery Beat is running.")
        else:
            print("Celery Beat is not running. State:",result.state)
    except Exception as e:
        print(f"Error checking Celery Beat health: {e}")

check_celery_beat_health()



"""

This are the states can be used 

PENDING: 
STARTED: 
SUCCESS: 
FAILURE: 
REVOKED: 
RETRY: 
IGNORED: 
RECEIVED: 
REJECTED: 
RECOVERED:
UNKNOWN: 

"""   