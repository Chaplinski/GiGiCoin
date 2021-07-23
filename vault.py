import random

class Vault:
    @staticmethod
    def does_hash_exist_on_disk(this_hash):
        flip = random.randint(0, 1)
        if flip == 0:
            print("True - " + str(this_hash) + " does exist on disk.")
        else:
            print("False - " + str(this_hash) + " does NOT exist on disk.")


v = Vault()
v.does_hash_exist_on_disk("123abc")
v.does_hash_exist_on_disk("456yhg")
v.does_hash_exist_on_disk("321kij")
v.does_hash_exist_on_disk("984rty")
v.does_hash_exist_on_disk("345oop")
v.does_hash_exist_on_disk("239iio")
v.does_hash_exist_on_disk("879jhd")
v.does_hash_exist_on_disk("306vcp")
