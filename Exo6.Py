size = input('enter a word : ')


if len(size) == 1:
    size = size * 6
if len(size) == 2:
    size = size[-1] + size[-2]
if len(size) == 3:
    size = size[-1] + size[0] + size[1]
if len(size) == 4:
    size = size[::-1]
if len(size) == 5:
    size = size[0] + 't' + size[1] + 't' + size[2] + 't' + size[3] + 't' + size[4] 
print(size)