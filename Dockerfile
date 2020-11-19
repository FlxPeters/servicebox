FROM python:3.8-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install dev dependencies
RUN apk update \
    && apk add bash curl postgresql-dev gcc python3-dev musl-dev openssl-dev libffi-dev

# Install poetry
RUN pip install -U pip \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /usr/src/app
COPY ./servicebox .
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

COPY ./docker/entrypoint.sh .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

# Start with internal server
# Should e replaced with Gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]