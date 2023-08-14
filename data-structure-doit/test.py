def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))
    print(f'{r:2} | {x:d}')

    while x > 0:
        print('   +'+(n+2) *'-')
        if x // r:
            print(f'{r:2} | {x//r:{n}} ... {x%r}')
        else:
            print(f'     {x//r:{n}} ... {x%r}')
        d += dchar[x % r]
        x //= r

    return d[::-1]

no = int(input('변환할 값 : '))
cd = int(input('진수 : '))

print(f'{no}는 {cd}진수로 {card_conv(no, cd)}입니다.')