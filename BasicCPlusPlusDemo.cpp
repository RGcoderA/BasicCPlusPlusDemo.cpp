//BasicCPlusPlusDemo.cpp
#include <iostream>

// Function declaration
int add(int a, int b);

int main() {
    // Variable declaration
    int x = 10;
    int y = 20;
    
    // Output
    std::cout << "Hello, World!" << std::endl;
    
    // Input
    std::cout << "Enter a number: ";
    std::cin >> x;
    
    // Control structure
    if (x > 10) {
        std::cout << "You entered a number greater than 10." << std::endl;
    } else {
        std::cout << "You entered a number less than or equal to 10." << std::endl;
    }
    
    // Function call
    int sum = add(x, y);
    std::cout << "The sum of " << x << " and " << y << " is " << sum << "." << std::endl;
    
    return 0;
}

// Function definition
int add(int a, int b) {
    return a + b;
}
