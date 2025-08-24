#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
#ifdef AZINO777
    freopen("in", "r", stdin);
#endif
    ios_base::sync_with_stdio(false); cout.setf(ios::fixed); cout.precision(20); cout.tie(nullptr); cin.tie(nullptr);
    int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        int n;
        cin >> n;
        int sm = 0;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            while (x) {
                sm += x % 10;
                x /= 10;
            }
        }
        if (sm % 3 == 0) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
    }
}
