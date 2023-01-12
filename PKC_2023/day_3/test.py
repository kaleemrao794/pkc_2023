# define the function that will calculate the age of the child to join the school
# def school_calculator(age, required_age_at_school=4):
#     if age==required_age_at_school:
#         print("congratulations! Fareha can join the school.")
#     elif age<=2:
#         print("You should take care of Fareha, she is still a baby")
#     elif age >=required_age_at_school and age <= required_age_at_school + 3:
#         print("Fareha should join the school")
#     elif age >= required_age_at_school + 3.5 and age <= required_age_at_school + 5:
#         print("Fareha should join the school, it is already too late")
#     elif age >= required_age_at_school + 6 and age <= required_age_at_school + 8:
#         print("Fareha should join primary school")
#     elif age >= required_age_at_school + 9 and age <= required_age_at_school + 11:
#         print("Fareha should join middle school")
#     elif age >= required_age_at_school + 12 and age <= required_age_at_school + 15:
#         print("Fareha should join secondary school")
#     elif age >= required_age_at_school + 16 and age <= required_age_at_school + 18:
#         print("Fareha should join college")
#     elif age > required_age_at_school + 18:
#         print("Fareha should join university")
#     else:
#         print("Fareha can not go to school")
# school_calculator(input("What is the age of your child? "))
def school_calculator(age, required_age_at_school=4):
    if age==required_age_at_school:
        print("congratulations! Your child can join the school.")
    elif age<=2:
        print("You should take care of your child, she is still a baby")
    elif age >=required_age_at_school and age <= required_age_at_school + 3:
        print("Your child should join the school")
    elif age >= required_age_at_school + 3.5 and age <= required_age_at_school + 5:
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

