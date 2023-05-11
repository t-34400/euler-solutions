#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>

bool isPrime(std::int64_t number, const std::vector<std::int64_t>& primes)
{
    auto isMultiple = [=] (std::int64_t prime) { 
        return number % prime == 0; };
    return std::find_if(primes.begin(), primes.end(), isMultiple) == primes.end();
}

int getNextPrime(std::int64_t prime, const std::vector<std::int64_t>& primes)
{
    std::int64_t number = prime + 1;
    while(!isPrime(number, primes)) {
        ++number;
    }
    return number;
}

int main() {
    std::int64_t target = 600851475143;
    auto maxPrime = target;

    std::int64_t prime = 2;
    std::vector<std::int64_t> primes = { prime };
    primes.reserve(100);

    while(prime * prime <= target) {
        while (target % prime == 0)
        {
            target /= prime;
            maxPrime = prime;
        }
        
        prime = getNextPrime(prime, primes);
        primes.push_back(prime);
    }

    std::cout << maxPrime << std::endl;
    return 0;
}