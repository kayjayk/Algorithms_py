import sys

tmp_str = sys.stdin.readline().strip()
tmp_list = tmp_str.split(' ')
l = len(tmp_list)
if tmp_list[0] == '':
    l = 0
print(l)