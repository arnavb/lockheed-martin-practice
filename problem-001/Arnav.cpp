#include <iostream>
#include <fstream>

int main()
{
    std::ifstream inputFile{ "Prob01.txt" };
    
    if (inputFile.is_open())
    {
        int numCases;
        inputFile >> numCases;
        
        inputFile.clear();
        inputFile.ignore();
        
        std::string currentLine;
        
        for (int i = 0; i < numCases; ++i)
        {
            getline(inputFile, currentLine);
        
            std::cout << currentLine << "\n" << currentLine << "\n";
        }   
    }
}