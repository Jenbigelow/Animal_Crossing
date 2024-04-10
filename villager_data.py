"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """


    species = set()
    file = open(filename)
    for line in file:
        total_animal_data = line.rstrip().split("|") 
        
        species.add(total_animal_data[1])
    file.close()
    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
    file = open(filename)

    for line in file: 
        name, species = line.rstrip().split('|')[:2]

        if search_string in ("All", species):
            villagers.append(name)
        

        

    # if search_string in 
        

    file.close()

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    total_animal_hobby_list =[[],[],[],[],[],[]]
    hobbies_names= ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    
    for name, _, _, hobby, _ in all_data(filename):
        for index, hobby_name in enumerate(hobbies_names): 
            if hobby_name == hobby:
                total_animal_hobby_list[index].append(name)
    
    [total_animal_hobby_list[num].sort() for num in range(len(total_animal_hobby_list))]

    return total_animal_hobby_list


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    file = open(filename)
    

    for line in file: 
        line = line.rstrip()
        total_data = line.split("|")
        
        all_data.append(tuple(total_data))
    

    file.close()
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    file = open(filename)

    for line in file: 
        line = line.rstrip()
        total_animal_data = line.split('|') 

        if villager_name == total_animal_data[0]:
            return total_animal_data[4]
        
    return None



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file  
        - villager_name (str): a villager's name 
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    personality_match = set([])
    total_data = all_data(filename)
    for index in range(len(total_data)):
        if villager_name == total_data[index][0]:
            villager_personality = str(total_data[index][2])
            print(villager_personality)
    
    for index in range(len(total_data)):
        if villager_personality == total_data[index][2]:
            personality_match.add(total_data[index][0])
    
    return personality_match

    



    # file = open(filename)

    # for line in file: 
        # line = line.rstrip()
        # total_animal_data = line.split('|') 
# 
        # if villager_name == total_animal_data[0]:
            # personality =  total_animal_data[2]
#   /          if personality == total_animal_data[2]:
                # personality_match.add(total_animal_data[2])
        
    # return personality_match
    

    

# file = open(filename)

    # for line in file: 
        # line = line.rstrip()
        # total_animal_data = line.split('|') 
        
        # likeminded= set()
        # perosnality = None
        # villagers_name = [2]
        # total_animal_data = [0]
        

        #for villagers_name in file: 
            #if name == villagers_name: 
                #personality == 
                