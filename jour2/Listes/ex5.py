scores = [45, 12, 78, 34, 90, 23, 67, 56, 89, 10]

# print(scores)

scores_copy1 = scores.copy()
scores_copy2 = scores.copy()

scores_copy1.sort()
scores_copy2.sort(reverse=True)

print(scores_copy1)
print(scores_copy2)

print(scores_copy2[:3])