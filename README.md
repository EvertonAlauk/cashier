# cashier
### A sample application that create a checkout
---

After all, you need to set the `PROVIDER_URL` in your environment variables which will be the endpoint that you will get the `url`, `auth` and `schema` data from provider.

This endpoint needs to return these values, being:

- a `string` for the `url`

- an `object` for the `auth` with:
    - `type` of auth (e.g. Header, URI)
    - `body` of auth (e.g. Bearer, Token)

- a `json schema object` for the `schema`

These three parameters will be usual for request data and create a checkout.

- The `url` will be the url for checkout.
- The `auth` is the way how your request will be authenticate.
- The `schema` will validate with `json schema` if your payload, sending by parameter in Cashier init, it's right.



```shell
docker build -t cashier -f Dockerfile .
```

```shell
docker run 
```

```python
cashier = Cashier(payload=payload)
if cashier.is_valid():
    cashier.create_checkout()
```

---

### Doing
- unit test

