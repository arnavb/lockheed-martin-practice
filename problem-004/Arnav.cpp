#include <iostream>
#include <fstream>
#include <string>

int getNum(int n)
{
    int prev2 = 0;
    int prev1 = 0;
    int current = 1;
    
    for (int i = 1; i < n; ++i)
    {
        prev2 = prev1;
        prev1 = current;
        current = prev2 + prev1;
    }
    
    return prev1;
}

int main()
{
    
    std::ifstream inputFile{ "Prob04.in.txt" };
    
    if (inputFile.is_open())
    {
        int numCases;
        inputFile >> numCases;
        
        for (int i = 0; i < numCases; ++i)
        {
            int fibN;
            inputFile >> fibN;
            std::cout << fibN << " = " << getNum(fibN) << "\n";
        }
    }
}