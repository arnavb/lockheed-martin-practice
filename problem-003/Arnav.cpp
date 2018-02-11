#include <iostream>
#include <fstream>
#include <string>

int main()
{
    
    std::ifstream inputFile{ "Prob03.in.txt" };
    
    if (inputFile.is_open())
    {
        int numCases;
        inputFile >> numCases;
        
        for (int i = 0; i < numCases; ++i)
        {
            int firstNum;
            int secondNum;
            
            inputFile >> firstNum >> secondNum;
            
            std::cout << (firstNum + secondNum) << " " << (firstNum * secondNum) << "\n";
        }
    }
}