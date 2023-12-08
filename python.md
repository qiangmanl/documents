#### yield
```python
#async
In [28]: import asyncio
    ...: 
    ...: async def async_generator():
    ...:     while True:
    ...:         i = input("input:")
    ...:         yield i
    ...:        # await asyncio.sleep(0) 
    ...: 
    ...: async def main():
    ...:     async for value in async_generator():
    ...:         print(value)
    ...: 
    ...: asyncio.run(main())


# generator 
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

for value in gen:
    print(value)

# werkzeug.local
In [1]: from werkzeug.local import Local

In [2]: local = Local()

In [3]: db = local("db")

In [4]: db
Out[4]: <LocalProxy unbound>

In [5]: local.db = 1

In [6]: db
Out[6]: 1

In [7]: local.db = 2

In [8]: db
Out[8]: 2


```




