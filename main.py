assignmentType = []

assignmentCount = int(input("How many assignment types do you have? "))
totalWeight = 0
weightedGrade = 0

for j in range(assignmentCount):
    print(f'For assignment type {j+1}:')
    weight = int(input(f'What is the weight of the assignment category? (percent) '))
    assignmentCount = int(input(f"How many assignments do you have? "))
    pointsPerAssignment = int(input("How many points per assignment? "))

    totalWeight += weight
    totalPoints = assignmentCount * pointsPerAssignment
    totalGrade = 0
    for i in range(assignmentCount):
        totalGrade += float(input(f"What was your grade for assignment number {i+1}? "))

    finalGrade = (totalGrade / totalPoints) * 100
    print(f'This categories grade is {finalGrade:.2f}% which is {weight}% of your grade for assignment number {j+1}.')
    weightedGrade += (finalGrade * weight)

actualGrade = (weightedGrade/totalWeight)
print(f'Your actual grade is {actualGrade:.2f}%. You have {totalWeight}% out of 100% for the grade weight.')