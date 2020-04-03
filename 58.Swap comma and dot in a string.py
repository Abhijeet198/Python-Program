# 58. Swap comma and dot in a string ///////

amount = "32.054,23"
maketran = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
