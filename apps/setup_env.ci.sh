echo DEBUG=$DEBUG >> ./.env

echo SECRET_KEY=$SECRET_KEY >> ./.env
echo DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 173.212.252.63 [::1]" >> ./.env
echo CELERY_BROKER=$CELERY_BROKER >> ./.env
echo CELERY_BACKEND=$CELERY_BACKEND >> ./.env


echo WEB_IMAGE=$WEB_IMAGE >> ./.env
echo CELERY_IMAGE=$CELERY_IMAGE >> ./.env
echo BEAT_IMAGE=$BEAT_IMAGE >> ./.env
echo DASH_IMAGE=$DASH_IMAGE >> ./.env
echo NGINX_IMAGE=$NGINX_IMAGE >> ./.env

# VIRTUAL HOST
echo VIRTUAL_HOST=$VIRTUAL_HOST  >> .env
echo VIRTUAL_PORT=$VIRTUAL_PORT  >> .env
echo LETSENCRYPT_HOST=$VIRTUAL_HOST  >> .env

# .env.proxy-companion for ssl
echo DEFAULT_EMAIL=$DEFAULT_EMAIL  >> .env.proxy-companion
#echo ACME_CA_URI=https://acme-staging-v02.api.letsencrypt.org/directory  >> .env.proxy-companion
echo NGINX_PROXY_CONTAINER=nginx-proxy  >> .env.proxy-companion