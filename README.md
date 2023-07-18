# storefront
A microservice architecture for an ecommerce platform. To (eventually) be deployed in dockerized containers/kubernetes cluster.

# ToDo/Roadmap
numbers are assigned as fib sequence
fib = [0, 1, 1, 2, 3, 5, 8, 13]
[starting db design](https://dbdocs.io/alex.johnson293/ecommerce?view=relationships) (note: some relationships incorrect & need fixing)
~~# Bootstrap project (1)~~
## establish API
# Create orders service (3)
  * ~~database models created, migration(s) applied~~
  * serializers created
  * create views (controller logic)
  * register urls (local & in parent app)
  * add test(s)
# Create user service (8 - lots of interconnected design)
  * ~~database models created, migration(s) applied~~
  * ~~serializers created~~
  * ~~create views (controller logic)~~
  * ~~register urls (local & in parent app)~~
  * add test(s)

# create product service (3)
  * ~~database models created, migration(s) applied~~
  * ~~serializers created~~
    * ~~product model~~
    * ~~product_category~~
    * ~~product_inventory~~
    * ~~discount~~
  * ~~register urls (local & in parent app)~~
  * add data to test api functionality
  * add test(s)



# build the front end (8)
# create login/auth endpoints (part of user service design)
* re-enable authorization protection (storefront/settings.py middleware)


# create controller service (13)
# dockerize
## deployment


## post-deploy

# forecast & create shipping service (5)
  * database models created, migration(s) applied
  * create simple template for testing
  * create views(controller logic)
  * register urls (local & in parent app)
  * add test(s)

## The (todo)Later Base
* [https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/](create timezone middleware/adjust default setting)
* create shipping application
* expand on current db model (ie add description to product table, etc)
* clean up tagged issues (commented as 'laterbase')
* clean up model names (django appends things like '_id' to keys, give a more readable alias or change the root name)

# notes
* django rest framework not working? open your IDE (in VSCode, `ctrl + shift + p`) and select `"python: select interpreter"`` and make sure the correct venv is active
* to verify jwt token: 
```shell
curl \ -X POST \ -H "Content-Type: application/json" \ -d "{\"email\": \"<email>\", \"password\": \"<password>\"}" localhost:8000/api/token/
```
in the response will be something like:
```
{"refresh":"<long string here>","access":"<another long string>"}
```
You can use the returned access token to prove authentication for a protected view:
```
curl \
  -H "Authorization: Bearer <access token>" \
  http://localhost:8000/api/products/
```
When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{\"refresh\":"<refresh token>"}' \
  http://localhost:8000/api/token/refresh/
```
For more notes on auth design: [read this](https://testdriven.io/blog/django-spa-auth/)

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
