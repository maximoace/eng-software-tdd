# |Takes a array of size n and sum all elements

# Max size limit
MAX_ARRAY_SIZE = 1000

class SizeError(Exception):
    pass

#Alias
Array = list[int]

def sum_of_array(array :Array):
    if not array or len(array) > MAX_ARRAY_SIZE:
        raise SizeError(f'Array size less than 0 or bigger than {MAX_ARRAY_SIZE}')

    sum = 0
    for item in array:
        if not isinstance(item, int):
            raise TypeError(f'{item} is not of type int.')
        sum += item

    return sum
