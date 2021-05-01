#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    unsigned long int N, L, K;

    cin >> N >> L;
    cin >> K;

    unsigned long int A[N];
    unsigned long int B[N];
    for (int i = 0; i < N; i++)
    {
        cin >> A[i];
        B[i] = L - A[i];
    }

    int score = 0;
    double max_length = double(L) / double(K);
}
