#---------------------BMI CALCULATORE-----------------------
class Bmi_Calculator:
     
    weightInkgs = 79
    hightInmeter = 4
    
    def cal_bmi(self):
        bm = (self.weightInkgs)/(self.hightInmeter)
        print(f"bmi is {bm}")
    
person1 = Bmi_Calculator()
person2 = Bmi_Calculator()
#---------------person2 detail--------------
person2.weightInkgs = 74
person2.hightInmeter = 3

#--------------printing-------------
print(f"person 1 weigh is :{person1.weightInkgs}")
print(f"person 1 hight is :{person1.hightInmeter}")
person1.cal_bmi()
print("------------------------------------",end="")

print(f"person 2 weight is{person1.weightInkgs}")
print(f"person 2 hight is{person1.hightInmeter}")
person2.cal_bmi()
# print(f"the bmi of person 2 is {person2.cal_bmi()}")