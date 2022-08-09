#include<iostream>
#include<string>

using namespace std;

const

int LCS(string s1, string s2)
{
    // print the LCS of s1 and s2
    int m = s1.length();
    int n = s2.length();
    int L[m+1][n+1];
    pair<int, int> parent[m+1][n+1];

    for(int i = 0; i <= m; i++)
    {
        for(int j = 0; j <= n; j++)
        {
            if(i == 0 || j == 0)
            {
                L[i][j] = 0;
                parent[i][j] = make_pair(-1, -1);
            }
            else if(s1[i-1] == s2[j-1])
            {
                L[i][j] = L[i-1][j-1] + 1;
                parent[i][j] = make_pair(i-1, j-1);
            }
            else
            {
                L[i][j] = max(L[i-1][j], L[i][j-1]);
                if(L[i-1][j] > L[i][j-1])
                    parent[i][j] = make_pair(i-1, j);
                else
                    parent[i][j] = make_pair(i, j-1);
            }
        }
    }
}

int main()
{
    string s1, s2;
    cin>>s1>>s2;
    cout<<LCS(s1.c_str(), s2.c_str(), s1.length(), s2.length())<<endl;
    return 0;
}
