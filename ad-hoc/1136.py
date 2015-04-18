#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# Apr 8 2015
# 1136 - Bingo!
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1136
#
# ad-hoc
#


while True:
    n, b = map(int, raw_input().split())

    if n == b == 0: break

    nums = map(int, raw_input().split())
    if 0 not in nums:
        print 'N'
        continue

    possibilities = set()
    for n1 in nums:
        for n2 in nums:
            possibilities.add(abs(n1 - n2))

    if len(possibilities) == n + 1:
        print 'Y'
    else:
        print 'N'
