
def kmp_match(txt: str, pat: str) -> int:
    pt = 1  # 패턴의 첫 문자 인덱스는 0이다
    pp = 0
    skip = [0] * (len(pat) + 1) # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0  # 패턴의 첫 문자 인덱스는 0이다
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp] # ???

    pt = pp = 0
    
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

s1 = input('텍스트를 입력하세요: ')
s2 = input('패턴을 입력하세요: ')

idx = kmp_match(s1, s2)

if idx == -1:
    print('텍스트 안에 패턴이 존재하지 않습니다')
else:
    print(f'{(idx+1)}번째 문자가 일치합니다.')

# KMP는 복잡하고 보이어무어보다 성능 면에서 좋지 않다. 따라서 실제 프로그램에서 거의 사용하지 않는다.