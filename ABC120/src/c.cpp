#include <iostream>

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;
    int N = s.length();
    int red = 0;
    int blue = 0;

    for (int i = 0; i < N; i++)
    {
        if (s[i] == '0')
        {
            red++;
        }
        else
        {
            blue++;
        }
    }
    if (red > blue)
    {
        cout << (2 * blue);
    }
    else
    {
        cout << (2 * red);
    }
    return 0;
}
