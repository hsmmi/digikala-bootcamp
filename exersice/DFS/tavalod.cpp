// include
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// function


// variable
const int MAXN = 5 * 1e5 + 5;
int n, m;
vector<vector<int> > G;
vector<int> group_size;

// get input
void getInput() {
    cin >> n >> m;
    G.resize(n);
    group_size.resize(n);    
    while(m --){
        int siz;
        cin >> siz;
        int u;
        cin >> u;
        u --;
        for (int i = 1; i < siz; i++) {
            int v;
            cin >> v;
            v --;
            G[v].push_back(u);
            G[u].push_back(v);
        }
        cout << "round " << m << " graph is:\n";
        for (int i = 0; i < n; i++) {
            cout << i << ": ";
            for (int j = 0; j < G[i].size(); j++) {
                cout << G[i][j] << " ";
            }
            cout << "\n\n";
        }
    }
}

int dfs(int u) {
    cout << "dfs " << u << "\n\n";
    int child_size = 1;
    group_size[u] = child_size;
    for (int v : G[u]) {
        if (group_size[v] == 0) {
            child_size += dfs(v);
        }
    }
    group_size[u] = child_size;
    cout << "in dfs\n";
    for(int i = 0; i < n; i++) {
        cout << group_size[i] << " ";
    }
    cout << "\n\n";
    return child_size;
}

void solve() {
    for(int i = 0; i < n; i++) {
        if (group_size[i] == 0) {
            dfs(i);
        }
        cout << "in main:\n";
        for(int i = 0; i < n; i++) {
            cout << group_size[i] << " ";
        }
        cout << "\n\n";
    }
}

// main
int main()
{
    getInput();
    solve();
    return 0;
}