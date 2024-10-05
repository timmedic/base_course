#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    cout << "Введите первый член геометрической прогрессии: ";
    int b1 = 0;
    cin >> b1;
    cout << "Введите знаменатель геометрической прогрессии: ";
    int q = 0;
    cin >> q;
    cout << "Введите кол-во членов геометрической прогрессии: ";
    int count = 0;
    cin >> count;

    for(int i = 1; i < count + 1; i++)
    {
        cout << i << ")" << b1 * pow(q, (i - 1)) << endl;
    }

    return 0;
}