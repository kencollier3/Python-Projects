KILOMETER_TO_MILE_CONVERSION = 1.60934
print('How many kilometers did you run today?')
kms = input()
miles = float(kms) / KILOMETER_TO_MILE_CONVERSION
print(f'Ok, you ran {round(miles, 2)} miles. Good job!')
