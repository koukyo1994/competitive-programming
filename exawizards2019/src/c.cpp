#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    int N, Q;
    cin >> N >> Q;
    string s;
    cin >> s;
    map<string, int> mp;
    for (int i; i < N; i++)
    {
        auto itr = mp.find((string)s[i]);
    }
}
