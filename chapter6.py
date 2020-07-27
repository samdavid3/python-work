susan_details = {'fname': 'Susan', 'lname': 'David',
                 'age': 50, 'city': 'Des Moines'}
print(susan_details)

programming_phrases = {'variable': 'changing values', 'loops': 'while statements',
                       'conditional': 'if statement', 'collection': 'arrays', 'key-value': 'dictionaries'}

print(f"the following are programming_phrases\n{programming_phrases['variable']}\n{programming_phrases['loops']}\n{programming_phrases['collection']}\n{programming_phrases['key-value']}")

# looping the dictionary
for term, meaning in programming_phrases.items():
    print(f'{term}:{meaning}')

programming_phrases['alphabetical order'] = 'sorted'
programming_phrases['unique list'] = 'set'

for term, value in programming_phrases.items():
    print(f'{term}:{value}')

water_bodies = {
    'nile': 'egypt',
    'missouri': 'america',
    'coovum': 'india'
}
for name, country in water_bodies.items():
    print(f'the {name} runs through {country}')
for name in water_bodies.keys():
    print(name)
for country in water_bodies.values():
    print(country)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
myList = []
for people in favorite_languages.keys():
    if (people == "jen" or people == "sarah"):
        myList.append(people)
myList.append('sam')
myList.append('susan')

for people in myList:
    if (people in favorite_languages.keys()):
        print(f'{people} has taken the poll')
    elif (people not in favorite_languages.keys()):
        print(f'{people} has taken the poll')
for hasto in favorite_languages.keys():
    if (hasto not in myList):
        print(f'{hasto}.....Please take the poll')

# Nesting
sam_details = {'fname': 'Sam', 'lname': 'David',
               'age': 50, 'city': 'Des Moines'}
dad_details = {'fname': 'Christian', 'lname': 'David',
               'age': 88, 'city': 'Chennai'}
people = [susan_details, sam_details, dad_details]
for person in people:
    print(person)
fav_places = {'India': 'Taj', 'America': 'Big Sur', 'Japan': 'Mt Fuji'}

susan_details['travel'] = 'india'
#people[0] = {'travel': 'India'}
print(susan_details)
