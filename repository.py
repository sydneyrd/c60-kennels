DATABASE = {
    "LOCATIONS" : [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
],

"EMPLOYEES": [
    {
        "id": 1,
        "name": "Jenna Solis",
        "address": "100 Infinity Way",
    }, {
        "id": 2,
        "name": "Jordan Nelson",
        "address": "500 Infinity Way",
    }, {
        "id": 3,
        "name": "Zoe LeBlanc",
        "address": "123 Main Street",
    }
],
"CUSTOMERS": [
    {
        "id": 1,
        "name": "Ryan Tanay",
        "address": "100 Infinity Way"
    }, {
        "id": 2,    
        "name": "Emma Beaton",
        "address": "500 Infinity Way",
    }, {
        "id": 3,
        "name": "Dani Adkins",
        "address": "123 Main Street"
    }
],

"ANIMALS": [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 3,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource.upper()]

def single(resource, id):
    """For GET requests to single resource"""
    response = None
    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for element in DATABASE[resource.upper()]:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if element["id"] == id:
            response = element

        return response


def create(resource, new_item):
    # Get the id value of the last animal in the list
    max_id = DATABASE[resource.upper()][-1]["id"]
    new_id = max_id + 1
    new_item["id"] = new_id
    # Add the animal dictionary to the list
    DATABASE[resource.upper()].append(new_item)
    pass
    # Return the dictionary with `id` property added
    return new_item
def delete(resource, id):
    """For DELETE requests"""
    element_index = -1
    for index, element in enumerate(DATABASE[resource.upper()]):
        if element["id"] == id:
            # Found the animal. Store the current index.
            element_index = index
    # If the animal was found, use pop(int) to remove it from list
    if element_index >= 0:
        DATABASE[resource.upper()].pop(element_index)
    pass

def update(resource, id, new_item):
    """For PUT requests"""
    for index, element in enumerate(DATABASE[resource.upper()]):
        if element["id"] == id:
            DATABASE[resource.upper()][index] = new_item
            break