class Trainer:
    def __init__(self, id: int, first_name: str, last_name: str, age: int, level: int):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, value: int) -> None:
        if isinstance(value, int):
            self.__id = value
        else:
            raise TypeError("El ID debe ser un entero")
       
   