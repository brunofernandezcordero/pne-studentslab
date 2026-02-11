if __name__ == '__main__' :
    with open('dna.txt') as f:
        data = f.read().replace('\n','')


def counting(data):
    count_dict = {}
    for i in data:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    print('Total length:', len(data))
    for letter in count_dict:
        print(f'{letter}: {count_dict[letter]}')
    return

counting(data)

# if __name__ == '__main__':
# prints to introduce the sequence, total length and each base count
