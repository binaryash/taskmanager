from __future__ import absolute_import, unicode_literals


# importing celery so it startes when django initializes
from .celery import app as celery_app

__all__ = ('celery_app',)
