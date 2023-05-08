using System;
using System.Linq;

class Answer
{
    static void Main()
    {
        var sum = Enumerable.Range(1, 999)
            .Where(x => (x % 3 == 0) || (x % 5 == 0))
            .Select(x => x)
            .Sum();
        Console.WriteLine(sum);
    }
}