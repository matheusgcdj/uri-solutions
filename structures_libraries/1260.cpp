/**
 * Uian Sol Gorgonio <sol.uian@gmail.com>
 * Apr 18 2015
 * 1260 - Especies de Madeira
 * https://www.urionlinejudge.com.br/judge/pt/problems/view/1260
 *
 * map
 */

#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main() {
    int num, total, repeat = 0;
    string tree;
    map <string, int> table;
    map <string, int>::iterator it;

    scanf("%d", &num);
    while (repeat < num + 2) {
        table.clear();
        total = 0;

        while (true) {
            getline(cin, tree);

            if (tree == "") {
                repeat++;
                break;
            }

            if (table.find(tree) == table.end())
                table[tree] = 1;
            else
                table[tree] += 1;

            total++;
        }

        if (table.size() > 0) {
            for (it = table.begin() ; it != table.end() ; it++) {
                cout << it->first << ' ';
                printf("%.4f\n", 100.0 * it->second/total);
            }
            if(repeat < num + 2)
                printf("\n");
        }
    }
    
    return 0;    
}
