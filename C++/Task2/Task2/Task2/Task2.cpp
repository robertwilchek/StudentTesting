#include <iostream>
#include <stdexcept>
#include <string>

void printLength(const std::string* textPtr)
{
    std::cout << "Length: " << textPtr->size() << std::endl;
}

int main()
{
    std::string* message = nullptr;
    printLength(message);

    std::cout << message << std::endl
}
