fun main() {
    val sum = (1 until 1000).filter { x -> 
        (x % 3 == 0) or (x % 5 == 0)
    }.sum()
    println(sum)
}