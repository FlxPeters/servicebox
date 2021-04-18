# ServiceBox

Simple, lean service inventory management.

**Some notes on the futur of this project:**

I started this project from a need to organize and maintain ownership and visibility of serivces in March 2020 because the was not other solution. 
At the same time Spotify released Backstage as open source project with an similar scope. 
This is a one man project and i can  not compete with a whole team at spotify. Also theit data model is much more mature. 

This project is not dead but more in an archive state. Feel free to use the code and ideas. 

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
