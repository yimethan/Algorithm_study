
while True:
    a, b, c = map(int, input().split())
    # 이 문제를 해결하기 위해선, 직각 삼각형인 것을 구분해야한다. 직각삼각형은 가장 큰 변의 길이의 제곱이 다른 두 변의 제곱의 합과 같다. 이걸 파악해야 하는데, 일단, 3개의 수 중에서 가장 큰 수를 고른다. 그 다음, 나머지 두 수를 제곱했해서 더 했을 때 같다면 직각삼각형이다.
    if a & b & c == 0:
        break;

    a_square = a * a
    b_square = b * b
    c_square = c * c

    if a_square == b_square + c_square:
        print("right")
    elif b_square == a_square + c_square:
        print("right")
    elif c_square == b_square + a_square:
        print("right")
    else:
        print("wrong")