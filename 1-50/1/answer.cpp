#include <iostream>

int getSumOfMultiples(int multiplicand, int maxNumber) {
    int multipleCount = maxNumber / multiplicand;
    return multiplicand * (multipleCount + 1) * multipleCount / 2; 
}

int main() {
    int maxNumber = 999;

    int sumOfMultiplesOf3 = getSumOfMultiples(3, maxNumber);
    int sumOfMultiplesOf5 = getSumOfMultiples(5, maxNumber);
    int sumOfMultiplesOf15 = getSumOfMultiples(15, maxNumber);

    std::cout << sumOfMultiplesOf3 + sumOfMultiplesOf5 - sumOfMultiplesOf15 << std::endl;

    return 0;
}