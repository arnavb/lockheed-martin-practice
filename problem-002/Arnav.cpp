#include <iostream>
#include <fstream>
#include <string>

int main()
{
    
    std::ifstream inputFile{ "Prob02.in.txt" };
    
    if (inputFile.is_open())
    {
        int numCases;
        inputFile >> numCases;
        
        for (int i = 0; i < numCases; ++i)
        {
            std::string currentWord;
            int removeIndex;
            
            inputFile >> currentWord >> removeIndex;
            
            currentWord.erase(currentWord.begin() + removeIndex);
            
            std::cout << currentWord << "\n";
        }
    }
}