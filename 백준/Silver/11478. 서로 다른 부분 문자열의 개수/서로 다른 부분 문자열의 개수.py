word = input()
partList = []

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        partList.append(word[i:j])

print(len(set(partList)))