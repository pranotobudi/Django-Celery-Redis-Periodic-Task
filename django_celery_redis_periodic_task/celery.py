import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_redis_periodic_task.settings')
app = Celery('django_celery_redis_periodic_task')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @app.task(name='example.say_hello')
# def say_hello():
#     print('Hello, World!')
# app.tasks.register('example.say_hello')

app.conf.beat_schedule = {
    'task-name': {
         'task': 'photos.tasks.task_save_latest_flickr_image', 
         'schedule': 10.0,
    },
    # 'task-name': {
    #      'task': 'photos.tasks.print_hello', 
    #      'schedule': 5.0,
    # },
        'every-second': {
        'task': 'example.say_hello',
        'schedule': 5.0,
    },
}



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
