from celery import Celery

app = Celery('your_project_name')

def check_celery_worker_health():
    try:
        result = app.send_task('celery.ping', queue='queue_name')
        
        if result.status == 'SUCCESS':
            print("Celery Worker is healthy.")
        else:
            print(f"Celery Worker is unhealthy. Status: {result.status}")
    except Exception as e:
        print(f"Error checking Celery Worker health: {e}")

check_celery_worker_health()
