class car():
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model



if __name__ == "__main__":
    carro = car("a", "b")
    print(carro)
