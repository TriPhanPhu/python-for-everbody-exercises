word = 'brontosaurus'

d = dict()
for c in word:
    if not c in d: 
        d[c] = 1
    else: 
        d[c] = d[c] + 1
print(d)

# Using the get method
d2 = dict()
for c in word:
    d2[c] = d2.get(c, 0) + 1
print(d2)
# Adding a comment
