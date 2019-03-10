#include <iostream>
#include <vector>

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, C;
    cin >> N >> M >> C;

    vector<int> B(M);
    vector<vector<int>> A(N, vector<int>(M));
    for (int i = 0; i < M; i++)
        cin >> B[i];

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
            cin >> A[i][j];
    }

    int count = 0;
    for (int i = 0; i < N; i++)
    {
        int temp = C;
        for (int j = 0; j < M; j++)
        {
            temp += A[i][j] * B[j];
        }
        if (temp > 0)
        {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
