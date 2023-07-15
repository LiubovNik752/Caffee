caffee = open('test_1.txt', encoding='utf-8')
lst = [x.split(' ') for x in caffee.read().split('\n')]
dictionary = dict(lst)

for key, value in dictionary.items():
    print(f'{key} {int(value) // 6}')
    dictionary[key] = int(value) // 6

key_max = max(zip(dictionary.values(), dictionary.keys()))[1]

winner = open('winner.txt', 'w', encoding='utf-8')
winner.write(key_max)

caffee.close()
winner.close()