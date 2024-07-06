while True:
    try:
        print(input())
    except:
        break

# sys.stdin.readline()을 사용하면 출력초과가 발생한다.
# input()는 EOF를 받을 때 EOFError가 발생한다.
# 그러나 sys.stdin.readline()은 EOF를 받을 때 빈 문자열을 반환한다.