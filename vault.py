import random
import sys

class Vault:
    def __init__(self):
        if len(sys.argv) > 2:
            if sys.argv[1] == "find":
                self.does_hash_exist_on_disk(sys.argv[2], sys.argv[3])

    @staticmethod
    def does_hash_exist_on_disk(this_hash, difficulty):
        flip = random.randint(0, 1)
        if flip == 0:
            print("True - " + str(this_hash) + " does exist on disk with difficulty " + str(difficulty))
        else:
            print("False - " + str(this_hash) + " does NOT exist on disk with difficulty " + str(difficulty))


v = Vault()