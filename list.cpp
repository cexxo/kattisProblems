"https://open.kattis.com/problems/listgame"
#include<iostream>
#include<cmath>
int main() {
    int s;
    std::cin >> s;
    int num_dividends = 0;
    
    // Check for divisibility by 2 separately
    while (s % 2 == 0) {
        num_dividends++;
        s = s / 2;
    }
    
    // Check for divisibility by odd numbers starting from 3
    for (int i = 3; i <= sqrt(s); i = i + 2) {
        while (s % i == 0) {
            num_dividends++;
            s = s / i;
        }
    }
    
    // If s is a prime number greater than 2
    if (s > 2) {
        num_dividends++;
    }
    
    std::cout << num_dividends;
    return 0;
}
