#include <iostream>
#include <vector>

using namespace std;

struct UnionFind
{
    // par[i]はiの親の番号
    vector<int> par;
    // 根ノードiに含まれるノードの数
    vector<int> sizes;

    // 最初は全てが根、サイズは0
    UnionFind(int N) : par(N), sizes(N)
    {
        for (int i = 0; i < N; i++)
        {
            par[i] = i;
            sizes[i] = 0;
        }
    }

    // xが属する木の根を再帰で得る
    int find(int x)
    {
        if (par[x] == x)
            return x;
        return par[x] = find(par[x]);
    }

    // データ xが含まれる木のサイズを返す
    int size(int x)
    {
        return sizes[find(x)];
    }

    // データxとデータyが同じグループにあるか判定する
    bool same(int x, int y)
    {
        return find(x) == find(y);
    }

    // 同じ親を持つならばマージする
    void unite(int x, int y)
    {
        x = find(x);
        y = find(y);

        if (x == y)
            return;

        if (size(x) < size(y))
        {
            par[x] = y;
            sizes[y] += sizes[x] + 1;
            sizes[x] = 0;
        }
        else
        {
            par[y] = x;
            sizes[x] += sizes[y] + 1;
            sizes[y] = 0;
        }
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> A(M);
    vector<int> B(M);
    vector<unsigned int> result(M);
    for (int i = 0; i < M; i++)
    {
        cin >> A[i] >> B[i];
        A[i]--;
        B[i]--;
    }

    UnionFind UF(N);
    result[M - 1] = N * (N - 1) / 2;
    for (int i = M - 1; i > 0; i--)
    {
        int size_a;
        int size_b;
        if (!UF.same(A[i], B[i]))
        {
            size_a = UF.size(A[i]) + 1;
            size_b = UF.size(B[i]) + 1;
        }
        else
        {
            size_a = 0;
            size_b = 0;
        }

        UF.unite(A[i], B[i]);
        result[i - 1] = result[i] - size_a * size_b;
    }
    for (int i = 0; i < M; i++)
        cout << result[i] << endl;

    return 0;
}
