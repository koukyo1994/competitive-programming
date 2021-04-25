#include <iostream>

void swap(char S[], int N)
{
    for (int i = 0; i < N; i++)
    {
        char a = S[i];
        char b = S[i + N];
        S[i] = b;
        S[i + N] = a;
    }
}

void swap_letter(char S[], int a, int b)
{
    char a_letter = S[a - 1];
    char b_letter = S[b - 1];
    S[a - 1] = b_letter;
    S[b - 1] = a_letter;
}

int main()
{
    int N, Q, T, A, B;
    std::cin >> N;
    char S[2 * N];
    std::cin >> S;
    std::cin >> Q;

    bool is_reversed = false;
    for (int i = 0; i < Q; i++)
    {
        std::cin >> T >> A >> B;
        if (T == 2)
        {
            is_reversed = !is_reversed;
        }
        else
        {
            int A_, B_;
            if (is_reversed)
            {
                if (A < N)
                    A_ = A + N;
                else
                    A_ = A - N;

                if (B < N)
                    B_ = B + N;
                else
                    B_ = B - N;
                swap_letter(S, A_, B_);
            }
            else
            {
                swap_letter(S, A, B);
            }
        }
    }

    if (is_reversed)
        swap(S, N);

    for (int i = 0; i < 2 * N; i++)
    {
        std::cout << S[i];
    }

    std::cout << std::endl;
}
