#include <iostream>

using namespace std;

int main()
{
    cout << "Введите число для определения его чётности/нечётности: ";
    int x = 0;
    cin >> x;

    if(x % 2 == 0)
    {
        cout << "Чётное" << endl;
    }
    else
    {
        cout << "Нечётное" << endl;
    }
    return 0;
}