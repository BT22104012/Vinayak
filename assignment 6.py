# Q 1

def perfect_number(n):
    divisors = []
    # Find all divisors of n
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    # Sum all divisors
    sum_divisors = sum(divisors)
    # Check if the sum of all divisors is equal to the number
    if sum_divisors == n:
        return True
    else:
        return False

# Test
print(perfect_number(6))

# Q 2

def is_palindrome(string):
    # Remove all non-alphanumeric characters
    string = ''.join(c for c in string if c.isalnum())

    # Convert the string to lowercase
    string = string.lower()

    # Reverse the string
    rev_string = string[::-1]

    # Check if the string is a palindrome
    if string == rev_string:
        return True
    else:
        return False

# Q 3

def pascal_triangle(n):
    # Iterate through every line
    # and print entries in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print(binomialCoeff(line, i),
                  " ", end="")
        print()

    # Function to calculate nCi


def binomialCoeff(n, i):
    res = 1
    if (i > n - i):
        i = n - i
    for k in range(0, i):
        res = res * (n - k)
        res = res // (k + 1)

    return res


# Driver Code
n = 5
pascal_triangle(n)

# Q4

def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False

    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))

# Q5

def sort_items(items):
    items = items.split('-')
    items.sort()
    return '-'.join(items)

print(sort_items("green-red-yellow-black-white"))

# Q 6

def student_data(student_id, student_name=None, student_class=None):
    if student_name and student_class:
        print('Student ID: {}'.format(student_id))
        print('Student Name: {}'.format(student_name))
        print('Student Class: {}'.format(student_class))
    else:
        print('Student ID: {}'.format(student_id))

student_data(1, 'John', 'A')
student_data(2)

# Q7
class Student:
    pass

class Marks:
    pass

# Instance of Student
std1 = Student()

# Instance of Marks
mrk1 = Marks()

# Check if std1 is instance of Student
print(isinstance(std1, Student))

# Check if mrk1 is instance of Marks
print(isinstance(mrk1, Marks))

# Check if Student is subclass of object
print(issubclass(Student, object))

# Check if Marks is subclass of object
print(issubclass(Marks, object))

# Q8

class SumZero:
    def __init__(self,nums):
        self.nums = nums

    def sumZero(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                for k in range(j + 1, len(self.nums)):
                    if(self.nums[i] + self.nums[j] + self.nums[k] == 0):
                        result.append([self.nums[i], self.nums[j], self.nums[k]])
        return result

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
sz = SumZero(nums)
print(sz.sumZero())

# Q 9

class Parentheses():

    def isValid(self, string):
        stack = []

        #Traverse through the string
        for char in string:
            #If the character is an opening bracket, push it to the stack
            if char in ["(", "{", "["]:
                stack.append(char)

            #If the character is a closing bracket
            else:
                #If the stack is empty, return False
                if len(stack) == 0:
                    return False

                #Pop the topmost element from the stack
                topElement = stack.pop()

                #Check if the popped element matches with the closing bracket
                if (topElement == "(" and char != ")"):
                    return False
                elif (topElement == "{" and char != "}"):
                    return False
                elif (topElement == "[" and char != "]"):
                    return False

        #If the stack is empty, return True
        if len(stack) == 0:
            return True
        else:
            return False