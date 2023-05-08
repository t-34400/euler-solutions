fun main() {
    val limit = 4000000
    var a = 0
    var b = 1
    var sum = 0

    while(b < limit) {
        val next = a + b
        if(next % 2 == 0) {
            sum += next
        }

        a = b
        b = next
    }

    println(sum)
}