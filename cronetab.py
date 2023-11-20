from crontab import CronTab

def add_cron_job(command, schedule):
    cron = CronTab(user='saikrishna')  
    job = cron.new(command=command)
    job.setall(schedule)
    cron.write()


def remove_cron_job(command):
    cron = CronTab(user='saikrishna')  
    for job in cron:
        if job.command == command:
            cron.remove(job)
    cron.write()

nginx_health_check = '/usr/bin/python3 /home/saikrishna/Desktop/scripts/scripts-health/nginx-_health.py >> /home/saikrishna/Desktop/scripts/scripts-health/output/nginx_output.txt 2>&1'


#add_cron_job(nginx_health_check, '*/1 * * * *')
remove_cron_job(nginx_health_check)