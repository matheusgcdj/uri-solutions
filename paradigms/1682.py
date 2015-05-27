#
# Uian Sol Gorgonio <sol.uian@gmail.com>
# May 1 2015
# 1682 - Codigo Genetico
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1682
#
# backtraking
#

import sys
sys.setrecursionlimit(10000)

genome_5000 = 'NONPNOPNPONOPNONPNOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPONPNONPONOPNONPNOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPONPNONPONOPNONPNOPNPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPONPNONPONOPNONPNOPNPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNOPNPONOPNONPNOPNPONOPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPONPNONPONOPNONPNOPNPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPONPNONPONOPNONPNOPNPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPOPNOPONOPNONPNOPNPONOPNONPNOPONOPNONPONOPNPONPNONPONOPNONPNOPNPONOPNONPONOPNPONPNONPONOPNONPNOPONOPNONPONOPNPOPNONPNOPNPONOPNONPNOPNPOPNONPNOP'
def solve(n, genome):
    global genome_5000

    if len(genome) == n:
        if compare_subsegments(genome):
            genome_5000 = genome
            return True
        else:
            return False
    else:
        if compare_subsegments(genome) and solve(n, genome + 'N'):
            return True
        elif compare_subsegments(genome) and solve(n, genome + 'O'):
            return True
        elif compare_subsegments(genome) and solve(n, genome + 'P'):
            return True
        else:
            return False

def compare_subsegments(genome):
    for length in xrange(1, len(genome) / 2 + 1):
        if genome[-2*length: -length] == genome[-length:]:
            return False
    return True


#solve(5000, '')
while True:
    n = int(raw_input())

    if n == 0: break

    print genome_5000[:n] 