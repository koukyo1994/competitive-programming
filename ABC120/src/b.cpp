#include <iostream>

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int A, B, K;
    cin >> A >> B >> K;
    int d;

    if (A > B)
    {
        d = A;
    }
    else
    {
        d = B;
    }

    int count = 0;
    while (count < K)
    {
        if (A % d == 0 && B % d == 0)
        {
            count++;
        }
        d--;
    }
    cout << (d + 1) << endl;
    return 0;
}
