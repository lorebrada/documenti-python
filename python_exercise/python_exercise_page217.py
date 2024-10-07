# esercizio numero 11.1 pagina 217 

"""A collection of functions for working with cities."""

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


# esercizio numero 11.2

def city_country(city, country, population):
    """Return a string like 'Santiago, Chile - population 5000000'."""
    output_string = f"{city.title()}, {country.title()}"
    output_string += f" -population {population}"
    return output_string



# esercizio numero 11.3 

class Employee:
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount

 