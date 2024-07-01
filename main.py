import time

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
special = ['!', '@', '#', '$', '%', '&', '(', ')', '?', '/', '+']


def customize():
    length = input("Enter your preferred length: ")

    if length.isnumeric() == False:
        print("Invalid length")
        return None
    else:
        length = int(length)

    complexity = input("Enter your preferred complexity:(E/M/H):\n"
                       "Easy: Only Uppercase and lowercase alphabets\n"
                       "Medium: Only Alphabets and Numbers\n"
                       "Hard: Alphabets, Numbers and Special Characters\n").upper()

    if complexity == "E":
        return length, complexity, True, True, False, False

    elif complexity == 'M' or complexity == 'H':

        doupper = input("Include Uppercase characters?(Y/N)").upper() == "Y"
        dolower = input("Include Lowercase characters?(Y/N)").upper() == "Y"

        if doupper == False and dolower == False:
            donum = True
        else:
            donum = input("Include Numbers?(Y/N)").upper() == "Y"

        dospecial = False

        if complexity == "M":
            return length, complexity, doupper, dolower, donum, dospecial

        if doupper == False and dolower == False and donum == False:
            dospecial = True
        else:
            dospecial = input("Include special characters? (Y/N) :").upper() == "Y"

        return length, complexity, doupper, dolower, donum, dospecial

    else:
        print("Invalid characters")


class randomize:
    def __init__(self, seed):
        self.lfsr = seed

    def rand(self):
        bit = ((self.lfsr >> 0) ^ (self.lfsr >> 2) ^ (self.lfsr >> 3) ^ (self.lfsr >> 5)) & 1
        self.lfsr = (self.lfsr >> 1) | (bit << 15)
        return self.lfsr

    def rand_in_range(self, range):
        return self.rand() % range


def generate(length, complexity, doupper, dolower, donum, dospecial):
    seed = int(time.time() * 1000) & 0xFFFF
    random = randomize(seed)
    password = ""

    while len(password) < length:
        i = random.rand_in_range(4 if dospecial else 3 if donum else 2)
        if i == 0 and doupper:
            password += upper[random.rand_in_range(25)]
        elif i == 1 and dolower:
            password += lower[random.rand_in_range(25)]
        elif i == 2 and donum:
            password += str(random.rand_in_range(10))
        elif i == 3 and dospecial:
            password += special[random.rand_in_range(11)]
    return password


l = customize()
regen = True
while regen != False:
    while l == None:
        l = customize()
    print(generate(*l))
    regen = input("Regenerate Password? (Y/N)").upper()
    if regen == "N":
        regen = False









