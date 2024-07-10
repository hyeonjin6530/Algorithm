result = ''

num, formation = map(int, input().split())

while(num%formation != num):
    remain = num % formation
    num = num // formation

    if remain < 10:
        result = str(remain) + result
    else:
        result = chr(remain + 55) + result

if num != 0:
    if num < 10:
        result = str(num) + result
    else:
        result = chr(num + 55) + result
    

print(result)