import string
import random

def gen_random_id(length:int=18) -> str:
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))