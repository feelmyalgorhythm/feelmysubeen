def solution(phone_book):
    dic = {}
    for num in phone_book:
        dic[num] = 1  # 기본 값

    for i in phone_book:  # ex. 123
        answer = ''
        for j in i:  # ex. 1/ 2/ 3
            answer += j
            # 하나씩 자른게 딕셔너리에 있는지 확인 (단, 본인은 아닌거)
            if (answer in dic) and (answer != i):
                return False  # 처음에 answer=True 하고 return answer해도 되지만 이게 더 빠름
    return True