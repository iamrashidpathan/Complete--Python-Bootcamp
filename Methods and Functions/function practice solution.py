# Warm up Section
# lesser of two evens


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    elif a > b:
        return a
    else:
        return b


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

# Animal cracker


def animal_cracker(string):
    words = string.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False


print(animal_cracker('Levelheaded Llama'))
print(animal_cracker('Crazy Kangaroo'))

# Makes twenty


def makes_twenty(a, b):
    if a + b == 20:
        return True
    elif a == 20 or b == 20:
        return True
    else:
        return False


print(makes_twenty(20, 10))
print(makes_twenty(2, 3))
print(makes_twenty(10, 10))

# Level 1
# Old Macdonald


def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize()


print(old_macdonald('macdonald'))

# Master Yoda


def master_yoda(text):
    return ' '.join(text.split()[::-1])


print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# Almost there


def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


print(almost_there(91))
print(almost_there(150))

# Level 2
# Find 33


def find_33(nums):
    for i in range(len(nums)):
        if nums[i:i+2] == [3, 3]:
            return True
    return False


print(find_33([3, 3]))

# Paper Doll


def paper_doll(text):
    text_out = ''
    for i in text:
        for j in range(3):
            text_out = text_out + i
    return text_out


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# Black Jack


def black_jack(a, b, c):
    abc = a+b+c
    if abc <= 21:
        return abc
    elif abc > 21 and (a == 11 or b == 11 or c == 11):
        abc = abc - 10
        if abc < 21:
            return abc
        else:
            return 'BUST'
    else:
        return 'BUST'


print(black_jack(5, 6, 7))
print(black_jack(9, 9, 9))
print(black_jack(9, 9, 11))

# Summer of '69


def summer_69(arr):
    add = True
    result = 0
    for i in arr:
        if i != 6:
            if add:
                result += i
            elif i == 9:
                add = True
        elif i == 6:
            add = False
    return result


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# Challenging Problems
# Spy Game


def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i] == 0:
            # print(i)
            # print(nums[i:i+3])
            if nums[i:i+3] == [0, 0, 7]:
                return True
    return False


print(spy_game([1, 0, 2, 0, 7]))
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4]))

