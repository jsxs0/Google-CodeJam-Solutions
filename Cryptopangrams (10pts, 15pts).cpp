#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <cstdio>
#include <set>
#include <unordered_map>

using namespace std;

long a[101];
long list[101];
set<long> s;
unordered_map<long, int> um;

long gcd(long a,long b)
{
    if(a%b==0)
        return b;
    else
        return gcd(b,a%b);
}

void solve() {
    memset(a, 0, sizeof(a));
    memset(list, 0, sizeof(a));
    s.clear();
    um.clear();
    long N, L;
    cin >> N >> L;
    for(long i = 0; i < L; ++i) {
        long tmp;
        cin >> tmp;
        a[i] = tmp;
    }

    for(long i = 1; i < L; ++i) {
        if(a[i] == a[i - 1]) continue;
        list[i] = gcd(a[i], a[i - 1]);
        int j = i - 1;
        while(j >= 0 && list[j] == 0) {
            list[j] = a[j] / list[j + 1];
            --j;
        }
        j = i + 1;
        while(j < L + 1 && list[j] == 0) {
            list[j] = a[j - 1] / list[j - 1];
            ++j;
        }
        break;
    }

    for(long i = 0; i < L + 1; ++i) s.emplace(list[i]);
    int c = 0;
    for(auto it = s.begin(); it != s.end(); ++it) um[*it] = c++;
    for(long i = 0; i < L + 1; ++i) {
        char cc = 'A' + um[list[i]];
        cout << cc;
    }
    cout << endl;
}

int main() {
    //freopen("../in", "r", stdin);
    //freopen("../out", "w", stdout);
    int T;
    cin >> T;
    for(int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
