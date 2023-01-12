# variables
ingredients = ['aalu', 'pyaz', 'maida', 'namak', 'hari_mirch', 'hara_dhania', 'anardana', 'oil']
price = [20, 200, 200, 20, 100, 40, 80, 500]

# pros:
# 1. It reduces the human effort
# 2. easy to write long code
# 3. easy to recall

# strategy:
# 1. Only those jo python ke liye reserved hai, use nahi karna hai
# i.e, if, for, while, class, def, try, except, finally, with, as, from, import, pass, break, continue, return, yield, del, global, nonlocal, assert, lambda, True, False, None, and, or, not, is, in, not in, is not, as, with, raise, assert, async, await, try, except, finally, if, elif, else, for, while, break, continue, return, yield, def, class, lambda, from, import, pass, nonlocal, global, del, True, False, None, and, or, not, is, in, not in, is not, as, with, raise, assert, async, await
# 2. don't ever write variable name with space
# 3. don't ever write variable name with capital letter
# 4. always use short name
# 5. don't ever use special character
# 6. don't ever use number in beginning
# 7. use meaningful name
# 8. use snake case(all words are separated by underscores, and the words are usually all lowercase.)
# 9. follow global variable naming convention
# 10. Don't repeat variable name
# 11. repeat variable name by assigning different number at the end

import pandas as pd
# form a dataframe
df = pd.DataFrame({'ingredients': ingredients, 'price': price})
print(df)
