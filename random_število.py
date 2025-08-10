import random
št1str = input("Vpišite spodnjo mejo obsega števil, ki jih bo računalnik lahko izbral: ")
št1int = int(št1str)
št2str = input("Vpišite zgornjo mejo obsega števil, ki jih bo računalnik lahko izbral: ")
št2int = int(št2str)
število = random.randint(št1int, št2int)
print (f"Naključno število je: {število}")