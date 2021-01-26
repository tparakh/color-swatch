# Color Swatch Backend App

## Getting started

#### Requirement

Make sure you have python and pip and run

    pip install virtualenvwrapper

Then create a virtualenv for this project

    mkvirtualenv colorswatch

This should switch you into that virtualenv, but in future run

    workon colorswatch

Now in the color-swatch directory run

    pip install -r requirements.txt

Run migrations using the default sqlite db

    python manage.py migrate

Finally the dev server can be run with

    python manage.py runserver

Backend API can be accessed at

    http://127.0.0.1:8000/api/color_swatch/v1/color_palette/