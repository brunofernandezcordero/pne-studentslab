def counting():
    base = input('Enter the base to be counted')
    count_dict = {}
    for i in base.upper():
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    print('Total length:',len(base))
    for letter in count_dict:
        print(f'{letter}: {count_dict[letter]}')
    return

counting()