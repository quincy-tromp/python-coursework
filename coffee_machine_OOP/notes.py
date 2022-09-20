from prettytable import PrettyTable

my_table = PrettyTable()
pokemons = ["Pikachu", "Charmander", "Squirtle"]
type = ["Electric", "Fire", "Water"]
my_table.add_column("Pokemon Type", pokemons)
my_table.add_column("Type", type)
print(my_table)
my_table.align = "l"
print(my_table)