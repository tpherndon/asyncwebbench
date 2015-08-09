Run flask via gunicorn:

    gunicorn -w 16 -b 0.0.0.0:8000 application:main
