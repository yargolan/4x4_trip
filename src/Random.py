
import uuid


def generate_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()).lower().replace("-", "")
    return random[0:string_length]
