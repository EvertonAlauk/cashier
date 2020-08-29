# cashier
### A sample application that create a checkout
---

```shell
docker build -t cashier -f Dockerfile .
```

```shell
docker run 
```

```python
cashier = Cashier(url=url, payload=payload, schema=schema)

if cashier.is_valid():
    if cashier.validate_schema():
        cashier.create_checkout()
```