input_file = open("input.txt", "r")
output_file = open("output.txt", "w")
line = input_file.readline().split()
n = int(line[0])
 
a = []
line = input_file.readline().split()
for i in range(n):
    a.append(int(line[i]))
m1 = a[0] + a[1] + a[n - 1]
m2 = a[n - 1] + a[n - 2] + a[0]

m = max(m1, m2)
for i in range(1, n - 1):
    if a[i] + a[i - 1] + a[i + 1] > m:
        m = a[i] + a[i + 1] + a[i - 1]
 
ans = m 
print(ans)