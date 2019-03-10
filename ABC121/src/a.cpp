#include <iostream>

int main()
{
    using namespace std;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    int h, w;
    cin >> H >> W;
    cin >> h >> w;

    int num_tile = H * W;

    num_tile -= h * W;
    num_tile -= H * w;

    num_tile += h * w;
    cout << num_tile << endl;

    return 0;
}
