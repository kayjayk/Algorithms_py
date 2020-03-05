import sys
import collections

word = sys.stdin.readline().rstrip().upper()
alpha_dict = collections.Counter(list(word))
dict_dict = collections.Counter(alpha_dict.values())
max_cnt = max(alpha_dict.values())

if dict_dict[max_cnt] > 1:
    print('?')
else:
    for key, value in alpha_dict.items():
        if value == max_cnt:
            print(key)
            break