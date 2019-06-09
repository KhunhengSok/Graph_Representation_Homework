class Vertex:
    def __init__(self, name):
        self._name = str(name) 

    def __eq__(self, value):
        return self._name == value._name

    def __str__(self):
        return f'{self._name}'

    def __hash__(self):
        return super().__hash__()
    
    