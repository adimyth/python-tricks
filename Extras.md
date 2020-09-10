## super
```python
class Animal:
    def __init__(self):
        print("Animal")

class Zebra:
    def __init__(self):
        super().__init__()
        # super(Zebra, self).__init__()
        # Animal.__init__(self)

zebra = Zebra()
```

## Functions
In Python, functions are first-class objects.
This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on).

## Impure Functions
Pure function take in an input & return an outptut. But impure functions have sideffects. For example-

`print()` - It returns None while having the side effect of outputting something to the console.
