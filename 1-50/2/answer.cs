using System;

class Answer 
{
    static void Main()
    {
        int limit = 4000000;
        int a = 0;
        int b = 1;
        int sum = 0;

        while(b < limit)
        {
            int next = a + b;
            if(next % 2 == 0)
            {
                sum += next;
            }

            a = b;
            b = next;
        }

        Console.WriteLine(sum);
    }
}