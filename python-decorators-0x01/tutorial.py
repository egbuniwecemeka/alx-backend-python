def sum(cube):
    total = cube * 3
    return total

print(sum(5))
print(sum(3))

# First-class Objects (Functional programming)
# Major concept is that functions can be passed around as arguments
def price_quantity(p, q): return p * q
def tot_price(tp, val1, val2): return tp(val1, val2)
print(tot_price(price_quantity, 4, 5))


# name decorator
def student(fname, lname):
    return f"Full name is {fname} {lname}"

def fullname(contact):
    return contact("Emmanuel", "Egbuniwe")

print(fullname(student))