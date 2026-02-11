
def average(list):
    count = 0
    for i in list:
        count += i
    avg = count / len(list)
    avg = round(avg,1)
    return avg

def days_above(list):
    above_list = []
    for i in list:
        if i > 17:
            above_list.append(i)
    return len(above_list)

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
sorted_temp = sorted(temperatures)

print("Wednesday:",temperatures[2])
print("Max:", max(temperatures))
print("Min:", min(temperatures))
print("Average:",average(temperatures))
print("Days above:",days_above(temperatures))
print("Sorted:", sorted_temp)