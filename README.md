# compose-ecobasa

This is a Docker Compose wrapper for the Ecobasa.org code resident in

- https://github.com/ecobasa/ecobasa

## Usage

1. `git clone https://lab.allmende.io/ecobasa/compose-ecobasa.git && cd compose-ecobasa`
1.1. Initialisation (see below)
2. `docker-compose up -d`

## Initialisation

```
docker-compose run --rm django ./manage.py syncdb --noinput
docker-compose run --rm django ./manage.py migrate
docker-compose run --rm django ./manage.py collectstatic --noinput
docker-compose run --rm django ./manage.py createsuperuser
```

## Update

If the sources in `./src` changed, please run this sequence of commands:

```
docker-compose build django
docker-compose run --rm django ./manage.py syncdb
docker-compose run --rm django ./manage.py migrate
rm -rf static-collected/*
docker-compose run --rm django ./manage.py collectstatic --noinput
docker-compose stop django && docker-compose rm -f django && docker-compose up -d django
```

## Development

You can use docker-compose.devel.yml and settings.devel.py to run a development environment
and then

```
docker-compose -f docker-compose.devel.yml build
docker-compose -f docker-compose.devel.yml run --rm django ./manage.py syncdb
docker-compose -f docker-compose.devel.yml run --rm django ./manage.py migrate 
docker-compose -f docker-compose.devel.yml run --rm django sh -c 'cd /opt/services/ecobasa/ecobasa/ && /opt/services/ecobasa/manage.py compilemessages'
docker-compose -f docker-compose.devel.yml up -d
```

## Licence

(c) 2019 Ecobasa e.V. - WTFPL
