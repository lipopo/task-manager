from invoke import tasks

from backend import app


@tasks.task
def run(c):
    app.run()
