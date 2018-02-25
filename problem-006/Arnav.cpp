#include <iostream>
#include <fstream>
#include <cctype>
#include <string>
#include <vector>
#include <unordered_map>

int main()
{
    std::unordered_map<char, std::string> pilotsAlphabet
    {
        { 'A', "Alpha" },
        { 'B', "Bravo" },
        { 'C', "Charlie" },
        { 'D', "Delta" },
        { 'E', "Echo" },
        { 'F', "Foxtrot" },
        { 'G', "Golf" },
        { 'H', "Hotel" },
        { 'I', "India" },
        { 'J', "Juliet" },
        { 'K', "Kilo" },
        { 'L', "Lima" },
        { 'M', "Mike" },
        { 'N', "November" },
        { 'O', "Oscar" },
        { 'P', "Papa" },
        { 'Q', "Quebec" },
        { 'R', "Romeo" },
        { 'S', "Sierra" },
        { 'T', "Tango" },
        { 'U', "Uniform" },
        { 'V', "Victor" },
        { 'W', "Whiskey" },
        { 'X', "Xray" },
        { 'Y', "Yankee" },
        { 'Z', "Zulu" }
    };
    
    
    std::ifstream inputFile{ "Prob06.in.txt" };
    
    if (inputFile.is_open())
    {
        int numCases;
        inputFile >> numCases;
        
        for (int i = 0; i < numCases; ++i)
        {
            int numRound;
            inputFile >> numRound;
            
            inputFile.ignore();
            
            std::vector<std::string> lines;
            for (int j = 0; j < numRound; ++j)
            {
                std::string currentLine;
                getline(inputFile, currentLine);
                
                lines.push_back(currentLine);
            }
            
            for (int i = 0; i < lines.size(); ++i)
            {
                for (int j = 0; j < lines[i].length() - 1; ++j)
                {
                    if (lines[i][j] == ' ')
                    {
                        std::cout << " ";
                    }
                    else
                    {
                        std::cout << pilotsAlphabet[std::toupper(lines[i][j])];
                        if (lines[i][j + 1] != ' ')
                        {
                            std::cout << '-';
                        }
                    }
                }
                std::cout << pilotsAlphabet[std::toupper(lines[i].back())] << "\n";
            }
        }
    }
}