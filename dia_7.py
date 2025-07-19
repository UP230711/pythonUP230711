# Variables iniciales
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. 
print("Length of it_companies:", len(it_companies))

# 2.
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# 3. 
it_companies.update(['Samsung', 'Intel', 'Cisco'])
print("After adding multiple companies:", it_companies)

# 4.
it_companies.remove('Oracle')
print("After removing Oracle:", it_companies)

# 5.
try:
    it_companies.remove('NonExistent')
except KeyError:
    print(" Error: 'NonExistent' not found using remove()")

it_companies.discard('NonExistent')
print(" discard() no lanza error si el elemento no existe")



# 1. 
print("Union A | B:", A.union(B))

# 2.
print("Intersection A & B:", A.intersection(B))

# 3. 
print("A subset of B:", A.issubset(B))

# 4. 
print("A and B are disjoint:", A.isdisjoint(B))

# 5.
print("A | B:", A | B)
print("B | A:", B | A)

# 6.
print("Symmetric difference A ^ B:", A.symmetric_difference(B))

# 7.
del A
del B




# 1.
age_set = set(age)
print("List length:", len(age))
print("Set length (unique values):", len(age_set))
print("Is list bigger than set?", len(age) > len(age_set))

# 2.
print("""
 string  → Secuencia de caracteres (inmutable)
 list    → Colección ordenada y mutable con duplicados
 tuple   → Colección ordenada e inmutable con duplicados
 set     → Colección no ordenada, sin duplicados y mutable
""")

# 3. 
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().replace('.', '').split()
unique_words = set(words)
print("Unique words:", unique_words)
print("Count of unique words:", len(unique_words))




