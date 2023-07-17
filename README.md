# storefront
A microservice architecture for an ecommerce platform. To (eventually) be deployed in dockerized containers/kubernetes cluster.

# ToDo/Roadmap
numbers are assigned as fib sequence
fib = [0, 1, 1, 2, 3, 5, 8, 13]
[starting db design](https://dbdocs.io/alex.johnson293/ecommerce?view=relationships) (note: some relationships incorrect & need fixing)

~~# Bootstrap project (1)~~
# Create orders service (3)
  * database models created, migration(s) applied
  * create simple template for testing
  * create views (controller logic)
  * register urls (local & in parent app)
  * add test(s)
# Create customer service (8)
  * database models created, migration(s) applied
  * create simple template for testing
  * create views (controller logic)
  * register urls (local & in parent app)
  * add test(s)
# create product service (3)
  * ~~database models created, migration(s) applied~~
  * serializer created
  * create simple template for testing
  * create views(controller logic)
  * register urls (local & in parent app)
  * add test(s)
# create controller service (13)
# forecast & create shipping service (5)
  * database models created, migration(s) applied
  * create simple template for testing
  * create views(controller logic)
  * register urls (local & in parent app)
  * add test(s)

## The (todo)Later Base
* [https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/](create timezone middleware/adjust default setting)
* 

## Setup

```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push

# Activate the environment
pipenv shell

```

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.
