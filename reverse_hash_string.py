string = input().split('#')
str_sorted = sorted(string,reverse=True)
result = '#'.join(str_sorted)
print(result,end='')
