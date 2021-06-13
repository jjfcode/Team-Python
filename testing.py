docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

if 'tuple' in docs:
    # do something
    print('tuple is here!')
else:
    # do something else
    print('tuple is not here!')

# Lo Mismo pero usando 'not in'

if 'tuple' not in docs:
    # do something
    print('tuple is not here!')
else:
    # do something else
    print('tuple is here!')

# cuanta veces tuple esta en la oracion

print(docs.count('tuple')) # Busca la palabra exacta
print(docs.index('tuple')) # lo encontro en la posicion 105