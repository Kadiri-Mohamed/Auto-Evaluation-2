text1 = '''Linear regression analysis is used to predict
the value of a variable based on the value of
another variable. The variable you want to
predict is called the dependent variable. The
variable you are using to predict the other
variable's value is called the independent
variable. This form of analysis estimates the'''

text2 = '''Logistic regression is a supervised machine
learning algorithm widely used for binary
classification tasks, such as identifying
whether an email is spam or not and diagnosing
diseases by assessing the presence or absence
of specific conditions based on patient test
results. This approach utilizes the logistic'''

set_text1 = set(text1.split())
set_text2 = set(text2.split())

res = [n for n in set_text1 & set_text2 if len(n) > 3]

print(res)