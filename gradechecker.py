class GradeList: # Represents a specific class
    def __init__(self):
        self.gradeList = []
        self.total = -1
        self.missingWeight = 0

    def addCategory(self, name=None, weight=0, points=0, total=None):
        category = Category(name, weight, points, total)
        self.gradeList.append(category)

    def appendCategory(self, category):
        self.gradeList.append(category)
    
    def calculateGrade(self): # Only modifies total and missingWeight
        total = 0
        currentWeight = 0 # When some categories may have no assignments yet
        for group in self.gradeList:
            if group.total == 0: # add EC category subclass
                continue
            total += group.weight * group.grade
            currentWeight += group.weight 
        self.total = total # range[0,100]
        self.total /= (currentWeight / 100)
        self.missingWeight = 100 - currentWeight

    def print(self):
        for group in self.gradeList:
            print(f'{group.name}: weight={group.weight:.2f}%,' 
                  f' grade={group.grade * 100:.2f}%, points={group.points:.2f}/{group.total:.2f},'
                  f' grade_contribution={group.weight * group.grade:.2f}%', end='')
            if self.missingWeight > 0:
                print(f', modified_grade_contribution={(group.weight * group.grade / (abs(self.missingWeight - 100) / 100)):.2f}%')
            else:
                print()
        self.calculateGrade()
        if self.missingWeight > 0:
            print(f'Missing Weight: {self.missingWeight:.2f}%')
        print(f'Total Grade: {self.total:.2f}%') # range[0,100]

class Category: # Represents grade category
    '''Usage: addCategory("Name", weight, points, total)'''
    def __init__(self, name=None, weight=0, points=0, total=None):
        self.name = name
        self.weight = weight # range[0,100]
        self.points = points
        self.total = total
        if self.total:
            self.grade = self.points / self.total # range[0,1]
        else:
            self.grade = 0 
    
    def updateGrade(self):
        self.grade = self.points / self.total

    def addPoints(self, num):
        self.points += num
        # Subtract points by adding num * -1
        self.updateGrade()

    def addAssignment(self, asgn_points, asgn_total):
        self.points += asgn_points
        self.total = asgn_total
        self.updateGrade()

class ExtraCreditCategory(Category):
    pass


def command_line_main():
    grades = GradeList()
    while True:
        option = input('ADD, EDIT, CALCULATE, CLEAR, or QUIT: ').upper()
        if option == 'ADD':
            className = input('Enter name of grade category, or quit: ').lower()
            if className == 'quit':
                continue
            classWeight = float(input('Enter weight of class category: '))
            classTotal = float(input('Enter total points of class category: '))
            classPoints = float(input('Enter your points in class category: '))
            newCat = Category(className, classWeight, classPoints, classTotal)
            grades.gradeList.append(newCat)

        elif option == 'EDIT':
            print('Choose a class to edit or quit: [', end='')
            nameMap = set()
            for group in grades.gradeList:
                print(f'{group.name} ', end='')
                nameMap.add(group.name)
            print(']', end='')
            editOption = input('').lower()
            if editOption == 'quit':
                continue
            elif editOption in nameMap:
                editCat = None
                editIndex = 0
                for group in grades.gradeList:
                    if editOption.casefold() == group.name.casefold():
                        editCat = group
                        break
                    editIndex += 1
                while(True):
                    catField = input('Edit name, weight, points, total, add assignment, delete, or quit').lower() 
                    if catField == 'name':
                        catName = input('Enter new name: ')
                        grades.gradeList[editIndex].name = catName
                    elif catField == 'weight':
                        catWeight = float(input('Enter new weight: '))
                        grades.gradeList[editIndex].weight = catWeight
                    elif catField == 'points':
                        catPoints = float(input('Enter new points: '))
                        grades.gradeList[editIndex].points = catPoints
                    elif catField == 'total':
                        catTotal = float(input('Enter new total: '))
                        grades.gradeList[editIndex].total = catTotal
                    elif catField == 'add':
                        catPoints = float(input('Enter your points: '))
                        catTotal = float(input('Enter assignment total: '))
                        grades.gradeList[editIndex].points += catPoints
                        grades.gradeList[editIndex].total += catTotal
                    elif catField == 'delete':
                        grades.gradeList.pop(editIndex)
                        break
                    elif catField == 'quit':
                        break


        elif option == 'CALCULATE':
            grades.print()
        elif option == 'CLEAR':
            grades.gradeList.clear()
        elif option == 'QUIT':
            break
