echo DEBUG=$DEBUG >> ./apps/.env

echo SECRET_KEY=$SECRET_KEY >> ./apps/.env
echo DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]" >> ./apps/.env
echo CELERY_BROKER=$CELERY_BROKER >> ./apps/.env
echo CELERY_BACKEND=$CELERY_BACKEND >> ./apps/.env