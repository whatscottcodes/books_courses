import random

# def ball_selection(listofBalls):
#     n = 0
#     result = []
#     listofBallsCopy = listofBalls[:]
#     while n < 3:
#         i = random.randint(0, len(listofBallsCopy)-1)
#         result.append(listofBallsCopy[i])
#         del listofBallsCopy[i]
#         n += 1
#     if sum(result) == 0 or sum(result) == 3:
#         return True
#
#
# def drawing_without_replacement_sim(numTrials):
#     '''
#     Runs numTrials trials of a Monte Carlo simulation
#     of drawing 3 balls out of a bucket containing
#     4 red and 4 green balls. Balls are not replaced once
#     drawn. Returns a float - the fraction of times 3
#     balls of the same color were drawn in the first 3 draws.
#     '''
#     results = 0
#     listofBalls = [0,0,0,0,1,1,1,1]
#     for i in range(numTrials):
#         if ball_selection(listofBalls):
#             results += 1
#     return results / numTrials
#
# print(drawing_without_replacement_sim(1000))


from itertools import product
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    res = np.zeros(len(choices), dtype=np.int)
    choices = np.array(choices)
    if total == 0:
        return res
    else:
        pos_res = list(product(range(2), repeat=len(choices)))
        for i in range(len(pos_res)):
            possibleResult = np.array(pos_res[i])
            res_check = sum(possibleResult * choices)
            cur_res = sum(res * choices)
            if res_check == total:
                if cur_res == total:
                    if sum(possibleResult) < sum(res):
                        res = possibleResult
                else:
                    res = possibleResult
            elif cur_res < res_check < total:
                res = possibleResult
            elif res_check == cur_res:
                if sum(possibleResult) < sum(res):
                    res = possibleResult
    return res

choices = [1,1,3,5,3]
total = 5
answer = [0,0,0,1,0]

print(find_combination([4, 6, 3, 5, 2], 10), np.array([1, 1, 0, 0, 0]))
ay = (np.array([4,6,3,5,2]) * np.array([0, 0, 1, 1, 1]))
print(sum(ay))


