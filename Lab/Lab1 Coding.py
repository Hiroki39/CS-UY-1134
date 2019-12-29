import random


def add_binary(bin_num1, bin_num2):
    result = ""
    carry = 0
    if len(bin_num1) < len(bin_num2):
        bin_num1, bin_num2 = bin_num2, bin_num1
    for i in range(1, len(bin_num1) + 2):
        if(i == len(bin_num1) + 1):
            if(carry == 0):
                return result
            else:
                result = str(carry) + result
                return result
        if i > len(bin_num2):
            submit = int(bin_num1[-i]) + carry
        else:
            submit = int(bin_num1[-i]) + int(bin_num2[-i]) + carry
        if(submit > 1):
            number = submit % 2
            carry = 1
        else:
            number = submit
            carry = 0
        result = str(number) + result


def can_construct(word, letters):
    lst = [0 for i in range(26)]
    for letter in letters:
        lst[ord(letter) - 97] += 1
    for letter in word:
        lst[ord(letter) - 97] -= 1
        if(lst[ord(letter) - 97] < 0):
            return False
    return True


def create_permutation(n):
    lst = []
    while(len(lst) < n):
        k = random.randint(0, n - 1)
        while(k in lst):
            k = random.randint(0, n - 1)
        lst.append(k)
    return lst


def scramble_word(word):
    lst = create_permutation(len(word))
    str = ""
    for i in lst:
        str = str + word[i]
    return str
