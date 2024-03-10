def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         backend=app.config['CELERY_RESULT_BACKEND'],
#         broker=app.config['CELERY_BROKER_URL']
#     )
#     celery.conf.update(app.config)
#     return celery

# app.config.update(
#     CELERY_BROKER_URL='url_to_your_broker',
#     CELERY_RESULT_BACKEND='url_to_your_backend'
# )
# celery = make_celery(app)