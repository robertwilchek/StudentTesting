// Task2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdexcept>
#include <string>

void printLength(const std::string* textPtr)
{
    // Pointer reference issue: this will dereference a null pointer when called with nullptr.
    std::cout << "Length: " << textPtr->size() << std::endl;
}

int main()
{
    std::string* message = nullptr;
    printLength(message);

    // Unhandled exception: the program will terminate because this exception is never caught.
    if (true)
    {
        throw std::runtime_error("Simulated failure in Task2");
    }

    std::cout << "This line is never reached" << std::endl
}
