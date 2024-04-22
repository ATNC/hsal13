import random
import string


def random_string(length: int = 10) -> str:
    """Generate a random string of fixed length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_dict_with_random_keys() -> dict:
    return {
        random_string(): random_string(50)
        for _ in range(100)
    }
