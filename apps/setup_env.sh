echo DEBUG=${secrets.DEBUG} >> .env

echo SECRET_KEY=${secrets.SECRET_KEY} >> .env
echo DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]" >> .env
echo CELERY_BROKER=${secrets.CELERY_BROKER} >> .env
echo CELERY_BACKEND=${secrets.CELERY_BACKEND} >> .env