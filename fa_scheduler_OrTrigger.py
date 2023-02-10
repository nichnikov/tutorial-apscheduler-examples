# https://pypi.org/project/fastapi-scheduler/
# https://itnext.io/scheduler-with-an-api-rocketry-fastapi-a0f742278d5b
# https://stackoverflow.com/questions/70104983/how-to-use-apscheduler-correctly-in-fastapi
"""
https://stackoverflow.com/questions/29429208/apscheduler-options

sched.add_job(my_job, trigger='cron', second='*') # trigger every second.
some more attributes
{'year': '*', 'month': 1, 'day': 1, 'week': '*', 'day_of_week': '*', 'hour': 0, 'minute': 0, 'second': 0}

How to use apscheduler to trigger job at specific times?
https://stackoverflow.com/questions/47764684/how-to-use-apscheduler-to-trigger-job-at-specific-times

"""
import time
import uvicorn
from fastapi import FastAPI
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI(title="SchedulerTesting")


def hello_world_print():
    print("Hello, Tutu", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


@app.on_event("startup")
def init_scheduler():
    scheduler = BackgroundScheduler()
    trigger = OrTrigger([CronTrigger(hour=14, minute=34), CronTrigger(hour=14, minute=35)])
    scheduler.add_job(hello_world_print, trigger)
    scheduler.start()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
