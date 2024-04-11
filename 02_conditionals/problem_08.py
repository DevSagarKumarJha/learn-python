password = "1234567"

pass_length = len(password)

if pass_length < 6:
  pass_strength = "Weak"
elif pass_length <=10:
  pass_strength = "Medium"
else:
  pass_strength = "Strong"

print(pass_strength)