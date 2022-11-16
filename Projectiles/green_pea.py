from pea import  Pea

class GreenPea(Pea):
    path = ''
    
    def __init__(self, position) -> None:
        super().__init__(position, 10, path)