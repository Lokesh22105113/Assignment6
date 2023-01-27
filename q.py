#ANSWER_1
# perfect number or not 
# test cases = 6 28 496 8128 
def main():
    user_input = int(input("Enter the number here - "))
    divisor_list = []
    sum = 0
    for i in range(1,user_input):
        if user_input % i == 0:
            divisor_list.append(i)
    for j in range(0 , len(divisor_list)):
        sum = sum + divisor_list[j]
    
    if sum == user_input:
        print("The number entered is a perfect number")
    else:
        print("The number entered is not a perfect number")
main()

#ANSWER_2
# passed string is palindrome or not
def main():
    user_input = str(input("Enter the string here - "))
    string = user_input.replace(" " , "")
    reverse = string[::-1]
    if reverse == string:
        print("The string is palindrome")
    else:
        print("The string is not a palindrome")
main()

#ANSWER_3
# first n rows of pascals triangle
from math import factorial
def main():
    rows = int(input("Enter the number of rows - "))

    for i in range(rows):
        for j in range(rows - i+ 1):
            print( end = " ")
        
        for t in range(i+1):
            answer = factorial(i)//(factorial(t) * factorial(i-t))
            print(answer , end = " ")
        print()
main()

#ANSWER_4
# string is a panagram or not (contains every word of the alphabet table )
def main():
    Input = str(input("Enter the string here - "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in Input.lower():
            flag = True
        else:
            flag = False
    if flag:
        print("Not Panagram")
    else:
        print("Panagram")
main()

#ANSWER_5
# sorting alphabetically
def main():
    input_string = str(input("Enter the string here - "))
    list = input_string.split("-")
    list.sort()
    for i in range(0 , len(list)):
        print(f"-{list[i]}" , end = " ")
        
    
main()

#ANSWER_6
def student_data(student_id , **kwargs):
    print(f"Student id is {student_id}")
    if "student_name" in kwargs:
        print(f"The student name is {kwargs['student_name']}")
    if "student_name" and "student_branch" in kwargs:
        print(f"The student name is {kwargs['student_name']} and branch is {kwargs['student_branch']}")

def main():
    
    student_data(student_id="22105079")
    student_data(student_id="22105079" , student_name="GAUTAM" , student_branch="ECE")

main()

#ANSWER_7
# instance or not and subclasses
def main():
    class student():
        pass
    class marks():
        pass
    student1 = student()
    marks1 = marks()
    print(isinstance(student1 , student))
    print(isinstance(marks1 , marks))
    print("Whether the said classes are subclasses of the built-in object class or not")
    print(issubclass(student , object))
    print(issubclass(marks , object))

main()

#ANSWER_8
# find the three elements that sum to zero from a set of n real number
def main():
    class solution():
        def findTriplets(self , list1 , n):
            list2 = []
            for i in range(0 , n-2):
                for j in range(i+1 , n-1):
                    for k in range(j+1 , n):
                        if list1[i] + list1[j] + list1[k] == 0:
                            a = list1[i]
                            b = list1[j]
                            c = list1[k]
                            list_number = [a , b ,c]
                            list2.append(list_number)
            print(list2)
            
    solution1 = solution()
    list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
    n = len(list1)
    solution1.findTriplets(list1 , n)
main()

#ANSWER_9
# validity of a string of parantheses
def check(sequence):
    for i in range(0,4):
        if "()" in sequence:
            sequence = sequence.replace("()" , "")
        elif "{}" in sequence:
            sequence = sequence.replace("{}" , "")
        elif "[]" in sequence:
            sequence = sequence.replace("[]" , "")
        else:
            return not sequence
def main():
    seq = "{{}{["
    print(f"if the set of parnatheses is correct? - {check(seq)}")
    seq2 = "(){}[]"
    print(f"if the set of parnatheses is correct? - {check(seq2)}")
main()
