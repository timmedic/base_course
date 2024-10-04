#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
    int N = 1;
    cout << "Введите число столбцов: ";
    cin >> N;
    int M = 1;
    cout << "Введите число строк: ";
    cin >> M;

    float trigonometry_array[M][N];
    for(int i = 0; i < M; i++)
    {
        for(int j = 0; j < N; j++)
        {
            trigonometry_array[i][j] = sin(N * i + M * j + 1);
            if(trigonometry_array[i][j] >= 0)   {cout << " ";}
            cout << fixed << setprecision(6) << trigonometry_array[i][j] << "||";
        }
        cout << "\n";
    }
    return 0;
}