required_age_at_school=4
fareha_age=3
# Qstn: can Fareha go to school?

if fareha_age==required_age_at_school:
    print("Fareha can join the school")

required_age_at_school=4
fareha_age=4
# Qstn: can Fareha go to school?

if fareha_age==required_age_at_school:
    print("Fareha can join the school")

required_age_at_school=4
fareha_age=3
# Qstn: can Fareha go to school?

if fareha_age==required_age_at_school:
    print("Fareha can join the school")
else:
    print("Fareha can not go to school")

required_age_at_school=4
fareha_age=30
# Qstn: can Fareha go to school?

if fareha_age==required_age_at_school:
    print("congratulations! Fareha can join the school.")
elif fareha_age<=2:
    print("You should take care of Fareha, she is still a baby")
elif fareha_age >=required_age_at_school and fareha_age <= required_age_at_school + 3:
    print("Fareha should join the school")
elif fareha_age >= required_age_at_school + 3.5 and fareha_age <= required_age_at_school + 5:
    print("Fareha should join the school, it is already too late")
elif fareha_age >= required_age_at_school + 6 and fareha_age <= required_age_at_school + 8:
    print("Fareha should join primary school")
elif fareha_age >= required_age_at_school + 9 and fareha_age <= required_age_at_school + 11:
    print("Fareha should join middle school")
elif fareha_age >= required_age_at_school + 12 and fareha_age <= required_age_at_school + 15:
    print("Fareha should join secondary school")
elif fareha_age >= required_age_at_school + 16 and fareha_age <= required_age_at_school + 18:
    print("Fareha should join college")
elif fareha_age > required_age_at_school + 18:
    print("Fareha should join university")
else:
    print("Fareha can not go to school")



