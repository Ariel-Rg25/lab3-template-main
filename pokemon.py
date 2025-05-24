from trainer import Trainer

class Pokemon:
    def __init__(self, id: int, name: str, weight: float, height: float, trainer: Trainer):
        self.__id = id
        self.name = name
        self.weight = weight
        self.height = height
        if isinstance(trainer, Trainer):
            self.trainer = trainer
        else:
            raise TypeError("El entrenador debe ser una instancia de la clase Trainer")

    def __str__(self) -> str:
        return self.name

    def get_id(self) -> int:
        return self.__id
    
    def set_id(self, value: int) -> None:
        if isinstance(value, int):
            self.__id = value
        else:
            raise TypeError("El ID debe ser un entero")

class ElectricPokemon(Pokemon):
    def __init__(self, id: int, name: str, weight: float, height: float, trainer: Trainer, electric_damage: int = 0):
        super().__init__(id, name, weight, height, trainer)
        self.electric_damage = electric_damage

    def attack(self) -> str:
        return f"{self.name} lanzó un ataque eléctrico!"

class FirePokemon(Pokemon):
    def __init__(self, id: int, name: str, weight: float, height: float, trainer: Trainer, fire_damage: int = 0):
        super().__init__(id, name, weight, height, trainer)
        self.fire_damage = fire_damage

    def attack(self) -> str:
        return f"{self.name} lanzó un ataque de fuego!"

class WaterPokemon(Pokemon):
    def __init__(self, id: int, name: str, weight: float, height: float, trainer: Trainer, water_damage: int = 0):
        super().__init__(id, name, weight, height, trainer)
        self.water_damage = water_damage

    def attack(self) -> str:
        return f"{self.name} lanzó un ataque acuático!"