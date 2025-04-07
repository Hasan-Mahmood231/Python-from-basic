def calculate_grade(mark):  
    if mark >= 90:  
        return "A+"  
    elif mark >= 86:  
        return "A"  
    elif mark >= 70:  
        return "B"  
    elif mark >= 60:  
        return "C"  
    elif mark >= 50:  
        return "D"  
    else:  
        return "Fail"   
  
sub1 = int(input("Enter the 1st subject marks: "))  
sub2 = int(input("Enter the 2nd subject marks: "))  
sub3 = int(input("Enter the 3rd subject marks: "))  
sub4 = int(input("Enter the 4th subject marks: "))  
sub5 = int(input("Enter the 5th subject marks: "))  
sub6 = int(input("Enter the 6th subject marks: "))  

marks = [sub1, sub2, sub3, sub4, sub5, sub6]  
grades = []  
gpa_total = 0  

for i in range(len(marks)):  
    grade = calculate_grade(marks[i])  
    if grade == 'A+':  
        gpa = 4.0  
    elif grade == 'A':  
        gpa = 4.0  
    elif grade == 'B':  
        gpa = 3.0  
    elif grade == 'C':  
        gpa = 2.7  
    elif grade == 'D':  
        gpa = 2.5  
    elif grade == 'F':  
        gpa = 2.0  
    else:  
        gpa = 0  
    gpa_total += gpa 
    grades.append(grade)  
    print(f"Grade for Subject {i + 1} with marks {marks[i]}: {grade}, GPA = {gpa}")  

overall_gpa = gpa_total /6   
print(f"Overall GPA: {overall_gpa}")  