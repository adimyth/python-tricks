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