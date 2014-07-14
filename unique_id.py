# random key generator
import string
import random
def unique_id_gen():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    
##How does it work ?
##
##We import string, a module that contains sequences of common ASCII characters, and random, a module that deals with random generation.
##
##string.ascii_uppercase + string.digits just concatenates the list of characters representing uppercase ASCII chars and digits:
##
##>>> string.ascii_uppercase
##'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##>>> string.digits
##'0123456789'
##>>> string.ascii_uppercase + string.digits
##'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
##Then we use a list comprehension to create a list of 'n' elements:
##
##>>> range(4) # range create a list of 'n' numbers
##[0, 1, 2, 3]
##>>> ['elem' for _ in range(4)] # we use range to create 4 times 'elem'
##['elem', 'elem', 'elem', 'elem']
##In the example above, we use [ to create the list, but we don't in the id_generator function so Python doesn't create the list in memory, but generates the elements on the fly, one by one (moreabout this here).
##
##Instead of asking to create 'n' times the string elem, we will ask Python to create 'n' times a random character, picked from a sequence of characters:
##
##>>> random.choice("abcde")
##'a'
##>>> random.choice("abcde")
##'d'
##>>> random.choice("abcde")
##'b'
##Therefore random.choice(chars) for _ in range(size) really is creating a sequence of size characters. Characters that are randomly picked from chars:
##
##>>> [random.choice('abcde') for _ in range(3)]
##['a', 'b', 'b']
##>>> [random.choice('abcde') for _ in range(3)]
##['e', 'b', 'e']
##>>> [random.choice('abcde') for _ in range(3)]
##['d', 'a', 'c']
##Then we just join them with an empty string so the sequence becomes a string:
##
##>>> ''.join(['a', 'b', 'b'])
##'abb'
##>>> [random.choice('abcde') for _ in range(3)]
##['d', 'c', 'b']
##>>> ''.join(random.choice('abcde') for _ in range(3))
'dac'
