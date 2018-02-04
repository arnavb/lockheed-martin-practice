#include <iostream>
#include <fstream>

int main()
{
    std::ifstream inputFile{ "Prob01.txt" };
    
    int numCases;
    std::cin >> numCases;
    
    for (int i = 0; i < numCases; ++i)
    {
        std::string currentLine;
        getline(inputFile, currentLine);
        
        
    }
}