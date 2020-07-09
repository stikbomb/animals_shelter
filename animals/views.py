from django.shortcuts import render

from .models import Animal, Image


def index(request):
    animals = Animal.objects.all()
    print(animals[0].__dict__)

    animals_collection = get_animal_collection(animals)

    data = {'animals': animals_collection}

    return render(request, 'index.html', context=data)


def animal(request, animal_id):
    pass


# def animal(request, animal_id):
#     place = get_object_or_404(Place, id=place_id)
#     return make_place_json(place)


def get_animal_collection(animals):
    result = {
        "animals": []
    }

    for animal in animals:
        stats = {
            "kind": animal.kind,
            "breed": animal.breed,
            "name": animal.name,
            "entry_date": animal.entry_date,
            "weight": animal.weight,
            "height": animal.height,
            "special_signs": animal.special_signs,
            "imgs": get_animal_images(animal.id)
         }

        result['animals'].append(stats)
    return result


def get_animal_images(animal):
    return [image.image.url for image in Image.objects.filter(animal=animal)]


def get_random_animals(count):
    pass


def get_all_animals():
    animals = Animal.objects.all()
    return animals
