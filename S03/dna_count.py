def counting(base):
    count_dict = {}
    base = base.replace(' ','')
    for i in base.upper():
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1

    return count_dict

if __name__ == '__main__': # “only run this code if this file is executed directly, not if it’s imported.”
    base = input('Enter the base to be counted')
    print('Total length:', len(base))
    count_dict = counting(base)
    for letter in count_dict:
        print(f'{letter}: {count_dict[letter]}')
