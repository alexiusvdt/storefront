# storefront
A microservice architecture for an ecommerce platform. To (eventually) be deployed in dockerized containers/kubernetes cluster.

Note that this is a work in progress & a clean, polished README with endpoint documentation will not be available until V1 release.


## The (todo)Later Base
* [https://docs.djangoproject.com/en/4.2/topics/i18n/timezones/](create timezone middleware/adjust default setting)
* create shipping application
* expand on current db model (ie add description to product table, etc)
* clean up tagged issues (commented as 'laterbase')
* clean up model names (django appends things like '_id' to keys, give a more readable alias or change the root name)

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
* generate a secret key
 use shell, save to your .env file

## Credits
This package was created with Cookiecutter and the [sourcery-ai/python-best-practices-cookiecutter](https://github.com/sourcery-ai/python-best-practices-cookiecutter) project template.

