# ServiceBox

Simple, lean service inventory management.

## What is ServiceBox

See: `/docs`

## Development

This project uses [Poetry](https://python-poetry.org/) as package manager.

**Start a dev server**

    poetry run python servicebox/manage.py runserver

**Make migrations**

    poetry run python servicebox/manage.py makemigrations

## Future features

- Validate services based on given rules like "A active service must have a source control link" or "An active service must have an monitoring link".
- Add event logs for stuff like maintenance or incidents
- Add a endpoint entity to document the endpoints of an service like an HTTP or TCP endpoint. This could be handy to provision a monitoring system like we do it with netbox as source for discovery source.

## Credits

ServiceBox is heavily inspired by Netbox and Jira's way of linking issues.
