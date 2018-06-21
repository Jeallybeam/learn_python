def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

#########################################################################################
#Passing Information to a Function
def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user('jesse')

#########################################################################################
#TIY
"""8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly."""
def display_message():
    print('We are learning about functions')

display_message()

#########################################################################################

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call."""
def favorite_book(title):

    print('Book title is: ' + title)

favorite_book('Potter')

#########################################################################################
#Positional Arguments
def describe_pet(animal_type, pet_name):
    """"Display information about a pet.""""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')


#########################################################################################
#Multiple Function Calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#########################################################################################
#Keyword Arguments


def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

#########################################################################################
#Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie', 'cat')

#########################################################################################
#TIY
"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments."""
def make_shirt(size,name):
    """Shirt params"""
    print('You ordered: ' + size + ' with this tex: ' + name)

make_shirt('xl', 'puppy')
make_shirt(name= 'cat', size= 'l')

#########################################################################################

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""
def make_shirt(size= 'XL',name= 'I Love Python'):
    """Shirt params"""
    print('You ordered: ' + size + ' with this tex: ' + name)

make_shirt()

#########################################################################################
"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""
def describe_city(city, country='chile'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'iceland')
describe_city('punta arenas')

#########################################################################################
#Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    print(full_name.title())

get_formatted_name('yar', 'tsiv')

#########################################################################################
#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


#########################################################################################
#Returning a Dictionary
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)

#########################################################################################
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#########################################################################################
#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#########################################################################################
# TIY
    """8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned."""


    def city_country(city, country):
	    """Return a string like 'Santiago, Chile'."""
	    return (city.title() + ", " + country.title())


    city = city_country('santiago', 'chile')
    print(city)

    city = city_country('ushuaia', 'argentina')
    print(city)

    city = city_country('longyearbyen', 'svalbard')
    print(city)

#########################################################################################
"""8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album."""
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

album = make_album('metallica', 'ride the lightning')
print(album)

album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)

#########################################################################################

"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop."""
################HOW TO ADD!!!!!!!!!!!!!!!!

def make_album(artist, title, tracks=0):
	"""Build a dictionary containing information about an album."""
	album_dict = {
		'artist': artist.title(),
		'title': title.title(),
	}
	if tracks:
		album_dict['tracks'] = tracks
	return album_dict


# Prepare the prompts. HOW TO ADD!!!!!!!!!!!!!!!!
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
	title = input(title_prompt)
	if title == 'quit':
		break

	artist = input(artist_prompt)
	if artist == 'quit':
		break

	album = make_album(artist, title)
	print(album)

print("\nThanks for responding!")

#########################################################################################
#Passing a List
def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
	    msg = "Hello, " + name.title() + "!"
	    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)