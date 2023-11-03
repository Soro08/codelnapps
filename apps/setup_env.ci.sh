echo DEBUG=$DEBUG >> ./.env

echo SECRET_KEY=$SECRET_KEY >> ./.env
echo DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]" >> ./.env
echo CELERY_BROKER=$CELERY_BROKER >> ./.env
echo CELERY_BACKEND=$CELERY_BACKEND >> ./.env