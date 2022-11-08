import string
import random
n = 8


def get_random_password() -> str:
    return "".join(random.sample((string.ascii_uppercase + string.ascii_lowercase + string.digits), n))


print(get_random_password())
