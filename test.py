# from password_preprocessor import pattern_calc, symbol_diff_calc 
# from random import randint

# ans = []
# rand = {str(i): [0] * randint(1, 4) for i in range(3)}
# with open("passwords.csv", "r") as csvfile:
#     data = csvfile.readlines()
#     smth = {"0": [], "1": [], "2": []}

#     for line in data[1:]:
#         password, score = line.replace("\n", "").split(",")
#         smth[score].append(password)
#     print(list(smth.keys()), list(rand.keys()), rand)
#     for indx in rand:
#         for x in range(len(rand[indx])):
#             rand[indx][x] = smth[indx][randint(0, len(smth[indx]))]
# print(rand)

d = [[4, 2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2], [2,2,2,2,2,2,2,2,2,2,3,3], [2,2,2,2,2,2,2,2,2,3,3,2], [2,2,2,2,2,2,2,3,3,4]]
ans = []

for line in range(4):
    ans.append({})
    for x in d[line]:
        for _ in range(x):
            ans[-1][input()] = (line, x)
        print("key is done")
    print("line is done")
print(ans)