#include <iostream>
#include <cstdint>

int main() {
    std::int32_t limit = 4000000;
    std::int32_t a = 0;
    std::int32_t b = 1;

    std::int32_t sum = 0;
    while(b < limit) {
        std::int32_t next = a + b;
        if(next % 2 == 0) {
            sum += next;
        }
        a = b;
        b = next;
    }

    std::cout << sum << std::endl;
    return 0;
}