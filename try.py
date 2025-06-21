def greet(city, age, name):
    print(f"Hello {name}, age {age}, from {city}.")

person = {"name": "Alice", "age": 30}

greet(**person, city="Mumbai")
