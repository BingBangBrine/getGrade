# include <tgmath.h>
# include <string>

# include <iostream>
# include <stdlib.h>
# include <vector>

using
namespace
std;

void
clearScreen()
{
    printf("\033[2J" "\033[1;1H");
}

int
main()
{
    clearScreen();

vector < int > categoriesValues;
cout << "How many assignments do you have? ";

int
assignmentCount;
cin >> assignmentCount;
cout << "How many points per assignment? ";

int
pointsPerAssignment;
cin >> pointsPerAssignment;

int
totalPoints = pointsPerAssignment * assignmentCount;
int
totalGrade = 0;

for (int i = 1; i <= assignmentCount; i++)
{
    cout << "what was your grade for number " << i << "? ";
int
grade;
cin >> grade;
totalGrade += grade;
cout << totalGrade << endl;
}

cout << assignmentCount << endl;
cout << totalPoints << endl;

int
finalGrade = (totalGrade / totalPoints) * 100;
// cout << endl << finalGrade << "%" << endl;
cout << (totalGrade / totalPoints) * 100 << "%" << endl;

return 0;
}