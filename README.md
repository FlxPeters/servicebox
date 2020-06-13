# ServiceBox

Simple, lean service inventory management.

## What is ServiceBox

ServiceBox aims to help you manage a growing amount of services.
It is a tool for the documentation of service oriented IT landscapes.

The basic idea is, that everyone in your organization is able to answer three simple questions about every service:

- **What** is deployed
- **Where** is it running
- **Who** is responsible

## Models

ServiceBox has a opinionated model to describe a landscape of services.
This model aims to be as simple as possible while also being able to describe all relevant details of a landscape.

### Services

A service is any kind of software or hardware that consists of one or more components to fully or partially fulfill a business process. This could be:

- a batch job
- web application
- message broker
- backup system
- storage system
- external software as a service tool

A service has a status to indicate its operational status and some fields for information related with the service. The model of services is based on the [runbook dialog sheet](https://github.com/SkeltonThatcher/run-book-template) and aims to give you a brief overview on how a service is designed and operated.

### Service relations

Most of these services cannot act as a standalone service and have dependencies to other services to fullfil their job. These dependencies are described with service relations. A relation has a type like "is related" or "depends on" and a description to define the context of the relation.

Service relations can be used to visualize dependencies and identify critical services in a landscape. They are also helpful for planing maintenance a get a tactical overview on which services are impacted by an incident.

### Platform

A platform is any kind of hosting environment in a given location.
A service always need a platform for hosting expect for SaaS services.

A platform could be:

- vSphere Cluster
- AWS Account or VPC
- Kubernetes Cluster
- Digital Ocean Account

Platforms are similar to services, but have a more defined purpose of hosting services, so we decided to model them as a separate entity. A Service gives you the answer to "What is deployed?", a platform should answer where a service is running.

Platforms can be organized by custom groups. For instance, you might create one group called "On premise" and one called "Cloud." The assignment of platforms to groups is optional. Groups can be nested within each other.

### Tenants

A tenant represents a discrete entity for administrative purposes. Typically, tenants are used to represent individual customers or internal departments within an organization.

A service and platform always needs a responsible tenant.
We distinguish different levels of responsibility:

- **Owner**: The owner tenant is responsible for all content decisions regarding a service.
- **Operator**: The operator tenant is responsible for operation the service from a technical perspective.
- **Support**: A service can have a support tenant which is responsible for problem solving and first level support.

Tenants can be organized by custom groups. For instance, you might create one group called "Internal" and one called "External." The assignment of tenants to groups is optional. Groups can be nested within each other.

### Links

ServiceBox only models the logical relationships between services and platforms. Additional documentation on deployment, configuration or runbooks is currently **not within the scope** of ServiceBox.

Nevertheless, the ServiceBox should be a central source of knowledge about services in the IT landscape. For this reason, web links can be attached to services and platforms.

A web link is similar to a service relation and has a type, description and URL. This could be:

- A Link to the source code of the service
- A link to a runbook
- A link to the moitoring dashboard od a service
- The login page of a platform

## Future features

- Validate services based on given rules like "A active service must have a source control link" or "An active service must have an monitoring link".
- Add event logs for stuff like maintenance or incidents
- Add a endpoint entity to document the endpoints of an service like an HTTP or TCP endpoint. This could be handy to provision a monitoring system like we do it with netbox as source for discovery source.

## Architecture

ServiceBox uses Django with Django-Rest as backend and a Vue.ja app as frontend. As persistance layer we use a relational database, mostly Postgres or SQLite for testing.

## Credits

ServiceBox is heavily inspired by Netbox, Jira.
