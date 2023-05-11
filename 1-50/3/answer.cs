using System;
using System.Collections.Generic;
using System.Linq;

class Answer 
{
    private static int getNextPrime(int prime, List<int> primes) 
    {
        var number = prime + 1;
        while(primes.Any(p => number % p == 0))
        {
            ++number;
        }
        return number;
    }

    static void Main()
    {
        long target = 600851475143L;
        var maxPrime = target;
        var prime = 2;
        var primes = new List<int>(100);
        primes.Add(prime);

        while(prime * prime <= target)
        {
            while(target % prime == 0)
            {
                target /= prime;
                maxPrime = prime;
            }

            prime = getNextPrime(prime, primes);
            primes.Add(prime);
        }

        Console.WriteLine(maxPrime);
    }

}