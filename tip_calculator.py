print('provide a bill and tip rate')

bill = float(input('enter bill: '))
tip_percentage = float(input('enter tip rate %: '))
tip_percentage = tip_percentage/100
tip = bill*tip_percentage
print('tip: $' + str(tip))
total = bill + tip
print('total bill: $' + str(total))
