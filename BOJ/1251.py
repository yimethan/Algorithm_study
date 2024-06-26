word = input()
least = 'z' * 51
for i in range(1, len(word) - 1):
    first = word[:i]
    for j in range(i+1, len(word)):
        second = word[i:j]
        third = word[j:]
        temp = first[::-1] + second[::-1] + third[::-1]
        if temp < least:
            least = temp
        
print(least)