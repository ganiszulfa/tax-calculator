# tax-calculator

## how to run

```
cd ./app
docker-compose up
```

## api doc

for demo purpose, no authentication required

add a new tax object

```
curl -X POST /api/tax_object/ -d '{"tax_code":integer, "amount":integer, "name":string}'
```

get a tax object
```
curl -X GET /api/tax_object/[tax object id]/
```

update a tax object
```
curl -X PUT /api/tax_object/[tax object id]/ -d '{"tax_code":integer, "amount":integer, "name":string}'
```

delete a tax object
```
curl -X DELETE /api/tax_object/[tax object id]/
```

get list of tax objects

```
curl -X GET /api/tax_object/
```

## db structure

for demo purpose, no relationship between user table and tax object table
```
User (based on django default user model)
-
Username PK string 
Password string 

TaxObject
-
Id PK int
Name int 
TaxCode int
Amount int 
TaxAmount decimal
TotalAmount decimal
```

## how to run the test
testing the
- env values
- tax calculation
- invalid tax code creation

```
docker-compose run django ./manage.py test
```
