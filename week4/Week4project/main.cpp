#include <iostream>
#include "math.h"

int main()
{

    int a{};
    int b{};
    std::cout << "enter 1 int:";
    std::cin >> a;
    std::cout << "\nenter 2 int:";
    std::cin >> b;
    std::cout << "ans:" << add(a, b);
};