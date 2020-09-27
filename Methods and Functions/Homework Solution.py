# 1 - Volume of a sphere


def vol(rad):
    return (4 / 3) * 3.14 * (rad**3)


print(vol(2))

# 2 - number in range


def ran_bool(num, low, high):
    return num in range(low, high+1)


print(ran_bool(10, 1, 10))

# 3 - no of uppercase and lowercase letters in a string


def up_low(s):
    d = {'upper':0, 'lower':0}
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass

    print("Original String : "+s)
    print("No of upper case letters: ", d['upper'])
    print("No of lower case letters: ", d['lower'])


up_low("My name Is Rashid")


# 4 - unique element list


def unique_list(lst):
    uni_list = []
    for i in lst:
        if i not in uni_list:
            uni_list.append(i)
    return uni_list


print(unique_list([1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 44, 5, 5, 5, 5, 6]))


# 5 - multiply numbers in list

def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


print(multiply([1, 2, 3, -4]))

# 6 - palindrome check


def palindrome(s):
    s_out = ''
    for w in s:
        if w == ' ':
            pass
        else:
            s_out += w
    return s_out[::-1] == s_out


print(palindrome('helleh'))
print(palindrome('nurses run'))

