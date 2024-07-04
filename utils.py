"""
Dark magic. Used to evaluate students. Feel free to read this code, but feel no need to understand it.

Please do not modify this file.
"""

import hashlib

def calculate_sha256(message):
    """
    Calculates a sha256. Avoids having us share HW answer keys while still letting students check their work.

    https://en.wikipedia.org/wiki/Cryptographic_hash_function

    :param message:
    :return:
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(message.encode(encoding="ascii"))
    return sha256_hash.hexdigest()