// include
#include <vector>
#include <iostream>

// class
class Graph
{
    public:
        int n;
        std:: vector<std:: vector<int> > G;
        Graph(int n) {
            this->n = n;
            G.resize(n);
        }
        void addEdge(int u, int v) {
            G[u].push_back(v);
            G[v].push_back(u);
        }
        std:: vector<int> neighbour(int u) {
            return G[u];
        }
        int size() {
            return n;
        }
};


// create class dfs that get graph
class DFS: public Graph
{ 

    // get graph
    public:
        DFS(int n): Graph(n) {}
        void dfs(int u) {
            visited[u] = true;
            for (int v : neighbour(u)) {
                if (!visited[v]) {
                    dfs(v);
                }
            }
        }
        std:: vector<bool> visited;
        void dfs_all() {
            visited.resize(n);
            for (int i = 0; i < n; i++) {
                if (!visited[i]) {
                    dfs(i);
                }
            }
        }
    
    
        std:: vector<int> order;
        int cnt;
        void dfs_visit(int u) {
            visited[u] = 1;
            for (int v : neighbour(u)) {
                if (!visited[v]) {
                    dfs_visit(v);
                }
            }
            order.push_back(u);
        }
};


// variable
const int MAXN = 5 * 1e5 + 5;
int n, b[MAXN], c[MAXN], cost = 0;
std:: vector<int> bombs;
Graph G1(n), G2(n);
bool visited[MAXN] = {false};


// function

// get input
void getInput() {
    std:: cin >> n;
    for (int i = 0; i < n; i++) {
        std:: cin >> b[i];
    }
    for (int i = 0; i < n; i++) {
        std:: cin >> c[i];
    }
    for (int u = 0; u < n; u++) {
        int v = b[u] - 1;
        G1.addEdge(u, v);
        G2.addEdge(v, u);
    }
    

}

void solve() {
    for(int i = 0; i < n; i++) {
        if(!visited[i]) {

            
        }
    }
}

// main
int main()
{
    getInput();
    solve();
    return 0;
}