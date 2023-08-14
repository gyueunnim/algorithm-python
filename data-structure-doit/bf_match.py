def bf_match(txt: str, pat: str) -> int:
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
        
    return pt - pp if pp == len(pat) else -1 # 성공 시, 패턴이 시작되는 텍스트의 인덱스

s1 = input('텍스트를 입력하세요: ')
s2 = input('패턴을 입력하세요: ')

idx = bf_match(s1, s2)

if idx == -1:
    print('텍스트 안에 패턴이 존재하지 않습니다')
else:
    print(f'{(idx+1)}번째 문자가 일치합니다.')


# 멤버십 연산자와 표준 라이브러리를 사용한 문자열 검색
# 멤버십 연산자: in, not in 
# ex) ptn (not) in txt: 문자열에 포함되어 있는지 판단할 수 있지만 위치는 알지 못한다
# 표준 라이브러리: find(), rfind(), index(), rindex()
# ex) str.find(sub[, start[, end]]): 문자열([strat:end])을 검색하여 검색한 문자열의 위치를 반환한다
# ex) str.startswith(prefix[, start[, end]]), endswith: 문자열이 다른 문자열의 시작이나 끝에 포함되어 있는지 판단

