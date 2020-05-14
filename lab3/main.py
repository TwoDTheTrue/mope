m = 5
y = [[5.1,5.4,5.3,5.5,5.2],
     [6.3,6.4,6.2,6.1,6.5],
     [7.5,7.3,7.4,7.2,7.1],
     [8.2,8.1,8.4,8.5,8.3]]
y_average = []
dispertion = []
for q in range(4):
    y_average.append(sum(y[q])/m)
    dispertion_current = 0
    for h in range(m):
        dispertion_current += (y[q][h]-y_average[q])**2
    dispertion.append(dispertion_current/(m-1))
print(dispertion)