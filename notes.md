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

# ToDo/Roadmap
numbers are assigned as fib sequence
fib = [0, 1, 1, 2, 3, 5, 8, 13]
[starting db design](https://dbdocs.io/alex.johnson293/ecommerce?view=relationships) (note: some relationships incorrect & need fixing)
~~# Bootstrap project (1)~~
## establish API
# Create orders service (3)
  * ~~database models created, migration(s) applied~~
  * ~~serializers created~~
  * ~~create views (controller logic)~~
  * ~~register urls (local & in parent app)~~
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
  * add test(s)

# refine API funcs
* currently all endpoints are just returning objects.all() and not modifying, selecting WHERE userid = user id, etc


# build the front end (8)
* scrollable design w/ nav
* subsections:
  * product listing
  * user portal (track orders, change pw, etc)
  * about the company
* login/out
* shopping portion (list of products)
* cart addon (small hover to view cart while browsing, separate page before purchase process starts)
* purchase process
* payment
* confirmation email sent
# create login/auth endpoints (part of user service design)
* re-enable authorization protection (storefront/settings.py middleware)


# create controller service (13)
# dockerize
## deployment


## post-deploy (aka ideas out of original scope)

# forecast & create shipping service (5)
  * database models created, migration(s) applied
  * create simple template for testing
  * create views(controller logic)
  * register urls (local & in parent app)
  * add test(s)

