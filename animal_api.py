""" Makes calls to animal API, pulls a random animal """
import requests


def get_animal():
    # get an animal (at random) for the user, which includes the name & a picture
    animal_url = "https://zoo-animal-api.herokuapp.com/animals/rand"
    response = requests.get(animal_url)
    animal_data = response.json()

    animal_picture = get_animal_picture(animal_data)
    animal_name = get_animal_name(animal_data)
    full_animal_info = [animal_name, animal_picture]

    # for testing - currently just shows the link to the animal pic in the terminal
    print(full_animal_info)

    return full_animal_info


def get_animal_picture(animal_data):
    #grabs the animal picture link from the API
    animal_picture = animal_data['image_link']

    return animal_picture


def get_animal_name(animal_data):
    #grabs the animals name from the API
    animal_name = animal_data['name']
    
    return animal_name
    
get_animal()