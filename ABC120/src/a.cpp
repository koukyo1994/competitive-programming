#include <iostream>

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int A, B, C;
    cin >> A >> B >> C;
    if (B / A > C)
    {
        cout << C;
    }
    else
    {
        cout << (B / A);
    }

    return 0;
}
