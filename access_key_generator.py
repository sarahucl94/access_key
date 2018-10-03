import random
import string

def generator():

    list_keys = []
    list_subjects = []
    length_key = 10
    name = input("Enter subject name: ")
    list_subjects.append(name)

    if name in list_subjects:
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=length_key))

    if key not in list_keys:
        list_keys.append(key)

    print(list_keys)
    print(list_subjects)


    with open('subject_keys.txt', 'a') as file:
        file.write(str((list_subjects + list_keys)))
        file.write('\n')
        file.close()

generator()