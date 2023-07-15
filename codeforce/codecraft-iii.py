months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = input()
left = int(input())
monthIndex = months.index(month)

print(months[(left + monthIndex) % 12])
