def count_j_in_st(J, S):
    jewels = set(J)
    count = sum(stone in jewels for stone in S)
    return count
J = input("Драгоценности: ")
S = input("Камни: " )
print(count_j_in_st(J, S))