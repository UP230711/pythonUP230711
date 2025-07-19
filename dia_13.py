# Level 1

import random
import math
from collections import Counter


def add_two_numbers(a, b):
    return a + b

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*args):
    if all(isinstance(x, (int, float)) for x in args):
        return sum(args)
    return "All items must be numbers."

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    return 'Invalid month'

def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2*a)
    x2 = (-b - d) / (2*a)
    return x1, x2

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    return rev

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    return sum(range(n+1))

def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

# Level 2

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f'The number of odds are {odds}.')
    print(f'The number of evens are {evens}.')

def factorial(n):
    return math.factorial(n)

def is_empty(param):
    return not bool(param)

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2)

def calculate_mode(lst):
    freq = Counter(lst)
    max_count = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_count]
    return mode

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean)**2 for x in lst) / len(lst)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))

# Level 3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def are_all_unique(lst):
    return len(lst) == len(set(lst))

def are_same_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

def most_spoken_languages(data, top=10):
    langs = []
    for country in data:
        langs.extend(country['languages'])
    return Counter(langs).most_common(top)

def most_populated_countries(data, top=10):
    sorted_data = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_data[:top]


def random_user_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))

def user_id_gen_by_user():
    num_chars = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    return [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=num_chars)) for _ in range(num_ids)]

def rgb_color_gen():
    return f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"



def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

def generate_colors(type_, n):
    if type_ == 'hexa':
        return list_of_hexa_colors(n)
    elif type_ == 'rgb':
        return list_of_rgb_colors(n)
    return []



def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def unique_random_numbers():
    return random.sample(range(10), 7)



def filter_negatives_and_zero(numbers):
    return [n for n in numbers if n <= 0]

def flatten_list_of_lists(list_of_lists):
    return [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]

def create_power_tuples():
    return [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

def flatten_country_data(countries):
    return [[country[0].upper(), country[0][:3].upper(), city.upper()] for pair in countries for (country, city) in pair]

def countries_to_dict(countries):
    return [{'country': country.upper(), 'city': city.upper()} for pair in countries for (country, city) in pair]

def names_to_strings(names):
    return [f"{first} {last}" for pair in names for (first, last) in pair]

def linear_lambda():
    return lambda x, m, b: m * x + b
