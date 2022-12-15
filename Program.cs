Console.WriteLine("Enter a number: ");
string number = Console.ReadLine();
int len = number.Length;

if (len == 5)
{
    if (number[0] == number[4] && number[1] == number[3])
    {
        Console.WriteLine($"{number} - Palindrome");
    }
    else
    {
        Console.WriteLine($"{number} - NOT A palindrome");
    }
}
else
{
    Console.WriteLine($"ERROR: {number} is not a five-digit");
}
