"""Celery config and tasks"""
import os
from datetime import datetime
from path import Path
from celery import Celery
from celery.schedules import crontab

SITE_NAME = Path(os.path.dirname(os.path.abspath(__file__))).name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings'.format(SITE_NAME))

app = Celery(
    SITE_NAME,
    broker='redis://localhost:6379/0',
    backend='django-db',
)

# load config from django settings, prefixed with CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# look for tasks.py in each app
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def heartbeat():
    print('celery beat is alive!')


def run_command(cmd):
    import subprocess
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


@app.task
def report_disk_usage():
    from django.core.mail import mail_admins
    mail_admins(
        'disk usage report at {}'.format(datetime.now()),
        run_command("df -h"),
    )


app.conf.beat_schedule = {
    'heatbeat': {
        'task': 'layout.celery.heartbeat',
        'schedule': 10,
    },
    'report_disk_usage': {
        'task': 'layout.celery.report_disk_usage',
        # http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
        'schedule': crontab(hour=0, minute=0),
    }
}
