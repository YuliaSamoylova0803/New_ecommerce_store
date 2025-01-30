class ZeroProduct(Exception):

    def __init__(self, message):
        super().__init__(message)

    # def __init__(self, *args, **kwargs):
    #     self.message = args[0] if args else "Нельзя добавить товар с нулевым количеством"

    # def __str__(self):
    #     return self.message