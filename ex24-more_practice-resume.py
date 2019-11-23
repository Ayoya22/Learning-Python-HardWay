# In this program we will apply most of the interesting things we have learned so far
print("Let's go through most of the cool stuff")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

phrase = """
\t What is the essence of life ? What is my role in this 
vast universe ?. The truth is we have a creator that
loves every bit of us and is ready to sacrifice himself for us.
 \nHis name is Jesus and he wants to be part of our life
now and for eternity.
"""
print("-----------------------")
print(phrase)
print("-----------------------")

ten = 30 - 20 + 40 -50 + 10
print(f"This should be ten: {ten}")

def testfunc(var1):
    tot_marks = 280
    avg = tot_marks / var1
    return tot_marks, var1, avg

val = 15
result = testfunc(val)
# Remember that this is another way of printing a string
print("The result is: {}".format(result))

