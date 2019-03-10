#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

template <typename Sequence, typename BinaryPredicate>
struct IndexCompareT
{
    IndexCompareT(const Sequence &seq, const BinaryPredicate comp)
        : seq_(seq), comp_(comp) {}
    bool operator()(const size_t a, const size_t b) const
    {
        return comp_(seq_[a], seq_[b]);
    }
    const Sequence seq_;
    const BinaryPredicate comp_;
};

template <typename Sequence, typename BinaryPredicate>
IndexCompareT<Sequence, BinaryPredicate>
IndexCompare(const Sequence &seq, const BinaryPredicate comp)
{
    return IndexCompareT<Sequence, BinaryPredicate>(seq, comp);
}

template <typename Sequence, typename BinaryPredicate>
std::vector<size_t> ArgSort(const Sequence &seq, BinaryPredicate func)
{
    std::vector<size_t> index(seq.size());
    for (int i = 0; i < index.size(); i++)
        index[i] = i;

    std::sort(index.begin(), index.end(), IndexCompare(seq, func));

    return index;
}

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long int N, M;
    cin >> N >> M;

    vector<int> A(N);
    vector<int> B(N);
    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i];
    }

    long int count = 0;
    long int money = 0;

    vector<size_t> sorted_index = ArgSort(A, less<int>());
    sort(A.begin(), A.end(), sorted_index);
    sort(B.begin(), B.end(), sorted_index);
    int idx = 0;

    while (count <= M)
    {
        if (M - count > B[idx])
        {
            money += A[idx] * B[idx];
            count += B[idx];
        }
        else
        {
            money += A[idx] * (M - count);
            count += (M - count);
        }
        idx++;
    }
    cout << money << endl;

    return 0;
}
