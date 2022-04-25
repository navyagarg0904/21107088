#Q1
number_1 = int(input("first number= "))                  #user enters input as integer
number_2 = int(input("second number= "))
number_3 = int(input("third number= "))
'''average = sum of all elements/total elements '''
average = (number_1 + number_2 + number_3)/3
print("entered values: ", number_1,",", number_2 ,",", number_3)
print("average of given values: ", average)


#Q2
Gross_income = float(input("Gross income(in $): "))
Dependents_in_family = int(input("Number of dependents in family: "))
Standard_deduction= 10000
Tax_rate = 0.2
Deduction_per_dependent = 3000
Taxable_income= Gross_income - Standard_deduction - (Deduction_per_dependent*Dependents_in_family)
Tax = Taxable_income*Tax_rate
print("Taxable_income: ",Taxable_income)
print("Tax: ",Tax)


#Q3
seconds = int(input("total number of seconds: "))
minutes = seconds//60
minute_seconds = seconds%60
print("hence", seconds, "seconds", "=", minutes, "minutes", minute_seconds, "seconds")


#Q4
number_01 = 25        #integer
number_02 = int('25')   #string value converted into integer
number_03 = int(25.0)     #float value converted into integer
sum = number_02 + number_02 + number_03
str(sum)          #result converted into string
print("sum: ", sum)


#Q5
import math  
'''pip install python_math
 math module was imported'''
i = 0
while i <= 345:                 #while loop used to make loop of 15degrees angles 
     sine = math.sin(math.radians(i))        
     cosine = math.cos(math.radians(i))
     print("sin(",i,"):", round(sine, 4), ",", "cos(",i,"):", round(cosine, 4))
     i += 15