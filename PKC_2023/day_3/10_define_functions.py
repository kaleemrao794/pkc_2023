# print("Hello sir! how are you?")
# print("Hello sir! how are you?")
# print("Hello sir! how are you?")

# # defining a function
# 1.
def print_greeting():
    print("Hello sir! how are you?")
    print("Hello sir! how are you?")
    print("Hello sir! how are you?")

print_greeting()

# 2.
def print_greeting():
    text = "Hello sir! how are you?"
    print(text)
    print(text)
    print(text)
print_greeting()

# 3.
def print_greeting(text):
    print(text)
    print(text)
    print(text)
print_greeting("Hello sir! how are you?")

# 4. defining a function with if elif else statements
def school_calculator(age, required_age_at_school=4):
    if age==required_age_at_school:
        print("congratulations! Your child can join the school.")
    elif age<=2:
        print("You should take care of your child, she is still a baby")
    elif age >=required_age_at_school and age <= required_age_at_school + 3:
        print("Your child should join the school")
    elif age >= required_age_at_school + 4 and age <= required_age_at_school + 5:
        print("Your child should join the school, it is already too late")
    elif age >= required_age_at_school + 6 and age <= required_age_at_school + 8:
        print("Your child should join primary school")
    elif age >= required_age_at_school + 9 and age <= required_age_at_school + 11:
        print("Your child should join middle school")
    elif age >= required_age_at_school + 12 and age <= required_age_at_school + 15:
        print("Your child should join secondary school")
    elif age >= required_age_at_school + 16 and age <= required_age_at_school + 18:
        print("Your child should join college")
    elif age > required_age_at_school + 18:
        print("Your child should join university")
    else:
        print("Your child can not go to school")
        
age = input("What is the age of your child? ")
age = int(age)
school_calculator(age)

# 5. defining a function for future
def future_age(age):
    new_age=age+20
    return new_age
    print(new_age)

# future_predicted_age=future_age(22)
# print(future_predicted_age)

