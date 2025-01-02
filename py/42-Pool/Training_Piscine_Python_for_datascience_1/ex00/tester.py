from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

tmp = [26, 18]

print(f"{height}\n{weight}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))

print(apply_limit(bmi, 26))

print(f"{tmp}")
print(apply_limit(tmp, 21))