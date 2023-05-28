def solution(clothes):
    ans = 1
    types = {}
    for i in clothes:  # type별로 딕셔너리 넣으면서 0의 값 주기 type이 key, values는 0
        types[i[-1]] = 0

    for k in clothes:
        types[k[-1]] += len(k[:-1])
        # print(k[:-1])
        # print(types[k[-1]])
        # print(types)
    for h in types.values():
        ans = (h + 1) * ans  # 안입는 개수도 세줘야 하니 +1을 해줌
    return ans - 1  # 전체에서 -1을 해주는 이유는 아예 안입는 경우의 수도 포함되어 있으므로
