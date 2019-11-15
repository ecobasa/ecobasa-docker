# start from an official image
FROM python:2.7

# arbitrary location choice: you can change the directory
WORKDIR /opt/services/ecobasa

# install our dependencies
ADD ./requirements.txt /opt/services/ecobasa/requirements.txt
RUN pip install -r requirements.txt

# copy our project code
COPY ./src /opt/services/ecobasa/

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--bind", ":8000", "ecobasa.wsgi:application"]

# getting image ready to compile translations
RUN apt-get update && apt-get install -y gettext libgettextpo-dev
