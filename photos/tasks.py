from celery.task.schedules import crontab
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from datetime import timedelta
from photos.utils import save_latest_flickr_image
from django_celery_redis_periodic_task.celery import app as celery_app
import celery 

logger = get_task_logger(__name__)


# @periodic_task(
#     #run_every=(crontab(minute='*')),
#     run_every=timedelta(seconds=10),
#     name="task_save_latest_flickr_image",
#     ignore_result=True
# )
@task(name="photos.tasks.task_save_latest_flickr_image")
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    save_latest_flickr_image()
    logger.info("|||||||||||||||||||||||||||||||||||||||")
    logger.info("PERIODIC TASK: SAVE IMAGE FROM FLICKR Saved image from Flickr")
     


@task(name='example.say_hello')
def say_hello():
    print('Hello, World!')


