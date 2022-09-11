"""
    File: pokemon.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Calculate the mediums of the pokemon's abilities
        and print the type with the max medium of the ability.
"""


def read_and_extract(filename):
    """
    Reads the file and extracts the data into the dictionary of dictionaries.

    Args:
        filename (str): The name of the file.

    Returns:
        dict: A dictionary of dictionaries that contains the data.

    Pre-condition:
        The file exists.

    Post-condition:
        The data is extracted into the dictionary of dictionaries.
    """
    lines = []
    pokemons = {}
    file = open(filename)
    data_lines = file.read().splitlines()
    for line in data_lines:
        lines.append(line.split(","))
    for i in range(1, len(lines)):
        pokemon_type = lines[i][2]
        pokemon_name = lines[i][1]
        pokemon_total = lines[i][4]
        pokemon_hp = lines[i][5]
        pokemon_attack = lines[i][6]
        pokemon_defense = lines[i][7]
        pokemon_special_attack = lines[i][8]
        pokemon_special_defence = lines[i][9]
        pokemon_speed = lines[i][10]
        if pokemon_type not in pokemons:
            pokemons[pokemon_type] = {}
        pokemon = {
            "total": pokemon_total,
            "hp": pokemon_hp,
            "attack": pokemon_attack,
            "defense": pokemon_defense,
            "special_attack": pokemon_special_attack,
            "special_defence": pokemon_special_defence,
            "speed": pokemon_speed,
        }
        pokemons[pokemon_type][pokemon_name] = pokemon
    return pokemons


def calculate_mediums(dataset):
    """
    Calculates the mediums of the pokemon's abilities.

    Args:
        dataset (dict): A dictionary of dictionaries that contains the data.

    Returns:
        dict: A dictionary of dictionaries that contains
            the mediums of the pokemon's abilities.

    Pre-condition:
        The dataset is a dictionary of dictionaries.

    Post-condition:
        The mediums of the pokemon types' abilities are calculated.
    """
    mediums = {}
    for pokemon_type in dataset:
        mediums[pokemon_type] = {}
        total_sum = 0
        hp_sum = 0
        attack_sum = 0
        defense_sum = 0
        special_attack_sum = 0
        special_defence_sum = 0
        speed_sum = 0
        for pokemon in dataset[pokemon_type]:
            total_sum += int(dataset[pokemon_type][pokemon]["total"])
            hp_sum += int(dataset[pokemon_type][pokemon]["hp"])
            attack_sum += int(dataset[pokemon_type][pokemon]["attack"])
            defense_sum += int(dataset[pokemon_type][pokemon]["defense"])
            special_attack_sum += int(dataset[pokemon_type][pokemon]["special_attack"])
            special_defence_sum += int(
                dataset[pokemon_type][pokemon]["special_defence"]
            )
            speed_sum += int(dataset[pokemon_type][pokemon]["speed"])
        mediums[pokemon_type]["total"] = total_sum / len(dataset[pokemon_type])
        mediums[pokemon_type]["hp"] = hp_sum / len(dataset[pokemon_type])
        mediums[pokemon_type]["attack"] = attack_sum / len(dataset[pokemon_type])
        mediums[pokemon_type]["defense"] = defense_sum / len(dataset[pokemon_type])
        mediums[pokemon_type]["special_attack"] = special_attack_sum / len(
            dataset[pokemon_type]
        )
        mediums[pokemon_type]["special_defence"] = special_defence_sum / len(
            dataset[pokemon_type]
        )
        mediums[pokemon_type]["speed"] = speed_sum / len(dataset[pokemon_type])
    return mediums


def print_type_with_max_medium_ability(ability, mediums):
    """
    Prints the type with the max medium of the ability.

    Args:
        ability (str): The name of the ability.
        mediums (dict): A dictionary of dictionaries that contains the mediums of the pokemon types' abilities.

    Returns:
        None

    Pre-condition:
        The ability is a string.
        The mediums is a dictionary of dictionaries.

    Post-condition:
        The types with the max medium of the ability is printed.
    """
    max_medium = 0
    pokemon_type = ""
    for type in mediums:
        if mediums[type][ability] > max_medium:
            max_medium = mediums[type][ability]
    types = []
    max_medium = 0
    for pokemon_type in sorted(mediums):
        if mediums[pokemon_type][ability] > max_medium:
            max_medium = mediums[pokemon_type][ability]
            types = [pokemon_type]
        elif mediums[pokemon_type][ability] == max_medium:
            types.append(pokemon_type)
    for pokemon_type in types:
        print("{}: {}".format(pokemon_type, mediums[pokemon_type][ability]))


def main():
    """
    The main function.

    Args:
        None

    Returns:
        None
    """
    file = input()
    dataset = read_and_extract(file)
    mediums = calculate_mediums(dataset)
    while True:
        command = input()
        if command == "":
            break
        elif command.lower() == "total":
            print_type_with_max_medium_ability("total", mediums)
        elif command.lower() == "hp":
            print_type_with_max_medium_ability("hp", mediums)
        elif command.lower() == "attack":
            print_type_with_max_medium_ability("attack", mediums)
        elif command.lower() == "defense":
            print_type_with_max_medium_ability("defense", mediums)
        elif command.lower() == "specialattack":
            print_type_with_max_medium_ability("special_attack", mediums)
        elif command.lower() == "specialdefense":
            print_type_with_max_medium_ability("special_defence", mediums)
        elif command.lower() == "speed":
            print_type_with_max_medium_ability("speed", mediums)
        else:
            continue


main()
