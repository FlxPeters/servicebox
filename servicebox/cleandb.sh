#! /bin/bash

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

rm db.sqlite3 

./manage.py makemigrations
./manage.py migrate

./manage.py shell --interface python < scripts/superuser.py
./manage.py shell --interface python < scripts/tenants.py
./manage.py shell --interface python < scripts/platforms.py
./manage.py shell --interface python < scripts/services.py
