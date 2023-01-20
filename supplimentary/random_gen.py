from random import choice, randint
location = [
    'tree',
    'flower',
    'fungi',
    'rock',
    'hill',
    'lake',
    'river',
    'field',
    'swamp',
    'cliff',
    'nest',
    'grove',
    'building',
    'bird',
    'mammal',
    'insect',
    'fish',
    'amphibian',
    'lizard',
    'human'
    ]
    
phenomena = [
    'A smiling',
    'A laughing',
    'A flying',
    'An inverted',
    'A musical',
    'A metallic',
    'A wooden',
    'A flickering',
    'A colour changing',
    'A big',
    'A small',
    'An electric'
    ]

effects = [
    'that alters time',
    'that alters gravity',
    'that screams',
    'that has information',
    'that moves differently',
    'that has a deck of cards',
    'that has extra legs',
    'that asks questions'
    ]
    
output = []
for a in range(10):
    output.append(f'{choice(phenomena)} {choice(location)} {choice(effects) if randint(1,100)<30 else ""}')
print(*output, sep='\n')
