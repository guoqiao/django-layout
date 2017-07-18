from layout.celery import app
from . import models as m


@app.task
def print_username(user_id):
    """A example task to talk to models"""
    user = m.UserProxy.objects.get(id=user_id)
    print(user.username)
