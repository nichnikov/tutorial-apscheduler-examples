# https://pypi.org/project/fastapi-scheduler/
# https://itnext.io/scheduler-with-an-api-rocketry-fastapi-a0f742278d5b
# https://stackoverflow.com/questions/70104983/how-to-use-apscheduler-correctly-in-fastapi
import uvicorn
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI(title="SchedulerTesting")


def hello_world_print():
    print("Hello")


@app.on_event("startup")
def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(hello_world_print, 'interval', seconds=5)
    scheduler.start()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
