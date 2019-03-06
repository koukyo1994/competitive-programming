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
