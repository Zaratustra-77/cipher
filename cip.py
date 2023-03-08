import random


def encrypt(text1):
    cipher1 = ['z', 'b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'n', 'v', 'w', 'x']
    cipher2 = ['e', 'o', 'i', 'y', 'm', 's', 'u', 'p', 'q', 't', 'a', 'r', 'g']
    c = 0
    new_message = ' '
    for i in text1:
        if i in cipher1:
            new_message += cipher2[cipher1.index(i)]
        elif i in cipher2:
            new_message += cipher1[cipher2.index(i)]
        elif i == ' ':
            new_message += str(random.randint(0, 9)) + random.choice(cipher1 + cipher2) + str(random.randint(0, 9))

    return new_message





def decrypt(text1):
    cipher1 = ['z', 'b', 'c', 'd', 'f', 'h', 'j', 'k', 'l', 'n', 'v', 'w', 'x']
    cipher2 = ['e', 'o', 'i', 'y', 'm', 's', 'u', 'p', 'q', 't', 'a', 'r', 'g']
    c = 0
    new_message = ''
    new_list = [i for i in text1]
    i = 0  # initialize index variable
    while i < len(new_list):
        if new_list[i] in cipher1:
            new_message += cipher2[cipher1.index(new_list[i])]
        elif new_list[i] in cipher2:
            new_message += cipher1[cipher2.index(new_list[i])]
        elif new_list[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            i += 2
            new_message += ' '
        elif new_list[i] == ' ':
            new_message += ''  # add a space to the decrypted message
            i += 3  # jump 3 positions ahead (to skip the letter, number, and space)
        i += 1  # always increment the index variable

    return new_message


# print(encrypt_decrypt('the time is now and we need to take a stand'))
if __name__ == '__main__':

    message = 'the time is now and we need to take a stand'
    scrambled_message = encrypt(message)
    print(scrambled_message)  # nsz0a0ncfz9p7ch9w4tbr9c2vty8w3rz0d4tzzy4c1nb6g6nvpz7x0v9z9hnvty
    unscrambled_message = decrypt(scrambled_message)
    print(unscrambled_message)  # the time is now and we need to take a stand
