echo DEBUG=$DEBUG >> ./.env

echo SECRET_KEY=$SECRET_KEY >> ./.env
echo DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 173.212.252.63 [::1]" >> ./.env
echo CELERY_BROKER=$CELERY_BROKER >> ./.env
echo CELERY_BACKEND=$CELERY_BACKEND >> ./.env


echo WEB_IMAGE=$WEB_IMAGE >> ./.env
echo CELERY_IMAGE=$CELERY_IMAGE >> ./.env
echo BEAT_IMAGE=$BEAT_IMAGE >> ./.env
echo DASH_IMAGE=$DASH_IMAGE >> ./.env