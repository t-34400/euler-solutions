import kotlin.collections.List
import kotlin.collections.MutableList


fun getNextPrime(primes: List<Long>): Long {
    var number = primes.last() + 1L
    while(primes.any{ number % it == 0L }) {
        number += 1L
    }
    return number
}

fun main() {
    var target = 600851475143L
    var maxPrime = target
    var primes = mutableListOf<Long>(2L)

    while(primes.last() * primes.last() <= target) {
        while(target % primes.last() == 0L) {
            target /= primes.last()
            maxPrime = primes.last()
        }

        primes.add(getNextPrime(primes))
    }

    println(maxPrime)
}