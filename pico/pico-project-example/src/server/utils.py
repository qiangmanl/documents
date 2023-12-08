import random
import string

def gene_rand_id(length:int=10)->str:
    characters = string.ascii_letters + string.digits 
    rand_id = ''.join(random.choice(characters) for _ in range(length))
    return rand_id
