# tax-calculator

## how to run

```
cd ./app
docker-compose up
```

## live demo

http://tax-calculator.ganis.pro

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

TBA
