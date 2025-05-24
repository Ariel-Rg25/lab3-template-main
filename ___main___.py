from pokemon import Pokemon, FirePokemon, ElectricPokemon, WaterPokemon
from trainer import Trainer

def classes_manual_tests():
    # Creación de entrenadores
    ash = Trainer(1, "Ash", "Ketchum", 10, 5)
    misty = Trainer(2, "Misty", "Erazo", 12, 11)
    brock = Trainer(3, "Brock", "Herrera", 18, 15)

    # Despliegue en pantalla de entrenadores
    print(ash)
    print(misty)
    print(brock)
    

    # Creación de pokémones
    pikachu = ElectricPokemon(25, "Pikachu", 6.0, 0.4, ash, 10)
    charmander = FirePokemon(4, "Charmander", 7.0, 0.5, brock, 8)
    squirtle = WaterPokemon(7, "Squirtle", 8.0, 0.6, misty, 7)

    # Despliegue de pokémones
    print(pikachu)  
    print(charmander)
    print(squirtle) 

    # Despliegue de ataques
    print("== Ataques ==")
    print(pikachu.attack())
    print(charmander.attack())
    print(squirtle.attack())


if __name__ == '__main__':
    classes_manual_tests()
