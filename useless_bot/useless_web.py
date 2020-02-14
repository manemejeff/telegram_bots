import random
from useless_bot.config import SITES


def get_random_url():
    useless_site = random.choice(SITES)
    return useless_site[0]
