word = input()
find = input()
start = cnt = 0

while start + len(find) <= len(word):
    if word[start: start + len(find)] == find:
        cnt += 1
        start += len(find)
    else:
        start += 1

print(cnt)