from sample_madlibs import code, hp, hungerGames, zombie
import random

if __name__ == "__main__":
    m = random.choice([code, hp, hungerGames, zombie])
    m.madlib()