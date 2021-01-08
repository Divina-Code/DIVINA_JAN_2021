

word = "hello"

# letters = list(word)
unic_letters = set(word)
print(unic_letters, len(unic_letters))


m1 = set((3, 7, 8, 9))
m2 = set((3, 7, 1, 2))

print(m1&m2)
print(m1-m2)
print(m2-m1)

print(m1|m2)

