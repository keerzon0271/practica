def combinationSum2(candidates, target):
    results = []
    candidates.sort()

    def backtrack(start, path, target):
        if target == 0:
            results.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            backtrack(i + 1, path + [candidates[i]], target - candidates[i])

    backtrack(0, [], target)
    return results

candidates1 = [2, 5, 2, 1, 2]
target1 = 5
result1 = combinationSum2(candidates1, target1)
print(result1)

candidates2 = [10, 1, 2, 7, 6, 1, 5]
target2 = 8
result2 = combinationSum2(candidates2, target2)
print(result2)