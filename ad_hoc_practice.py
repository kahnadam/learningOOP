# Try out some built in functions

#this one seems to return 1 if x > y, 0 if x == y, and -1 if x < y:
def compare(x,y):
    return cmp(x,y)

print compare(4,7)

# enumerate returns the count starting from 0 and values of a list
seasons = ['Spring','Summer','Fall','Winter']
print list(enumerate(seasons))


# convert integer to octal string
print oct(7)
print oct(8)
print oct(9)
print oct(10)

# return x to the power y
print pow(3, 2)

# return x to the power y, modulo z
print pow(4, 3, 61)
# 4^3 = 64
# 64 / 61 = 1, remainder 3
# so this will return "3"
