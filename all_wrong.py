# There's a multiple-choice test with N questions, numbered from 1 to N. Each question has 2 answer options, labelled A and B. You know that the correct answer for the ith question is the ith character in the string C, which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly. 
# Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters, the ith of which is the answer you should give for question i in order to get it wrong (either "A" or "B").

# Sample test case #1
# N = 3
# C = ABA
# Expected Return Value = BAB

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  transtable = C.maketrans("AB", "BA")
  txt_replace = C.translate(transtable)
  return txt_replace