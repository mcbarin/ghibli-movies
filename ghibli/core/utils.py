import requests

class Person:
    def __init__(self, id, name, gender, age, eye_color, hair_color, films, species, url):
        self.id = id
        self.name = name
        self.gender = gender
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.films = films
        self.species = species
        self.url = url


class Movie(object):
    def __init__(self, id, title, description, director, producer, release_date, rt_score, species, locations, vehicles, url):
        self.id = id
        self.title = title
        self.description = description
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.rt_score = rt_score
        self.people = []
        self.species = species
        self.locations = locations
        self.vehicles = vehicles
        self.url = url
    
    def add_person_to_people(self, person):
        self.people.append(person)


def get_movies_from_ghibli():
    response = requests.get("https://ghibliapi.herokuapp.com/films")
    if response.status_code == 200:
        return response.json()
    return None


def get_people_from_ghibli():
    response = requests.get("https://ghibliapi.herokuapp.com/people")
    if response.status_code == 200:
        return response.json()
    return None


def get_movies_with_people():
    movies = get_movies_from_ghibli()
    people = get_people_from_ghibli()

    movie_map = {}
    people_list = []

    for movie in movies:
        m = Movie(
            movie['id'],
            movie['title'], 
            movie['description'], 
            movie['director'], 
            movie['producer'], 
            movie['release_date'], 
            movie['rt_score'], 
            movie['species'], 
            movie['locations'], 
            movie['vehicles'], 
            movie['url']
        )
        movie_map[m.url] = m


    for person in people:
        p = Person(
                person['id'],
                person['name'],
                person['gender'],
                person['age'],
                person['eye_color'],
                person['hair_color'],
                person['films'],
                person['species'],
                person['url']
        )
        for film in p.films:
            movie_map[film].add_person_to_people(p)
    
    return movie_map.values()
