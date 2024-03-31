A = 1
B = 2
C = 3
X = 20
Y = 10
Z = -1

V1 = True
V2 = False

Nome = 'Pedro'
Rua = 'Pedrinho'

print(A + C / B) ##2,5
print(C / B / A) ##1,5
print(-X ** B) ##-400
print((-X) ** B) ##400
print(V1 or V2) ##True
print(V1 and not V2) ##True
print(V2 and not V1) ##False
print(not Nome == Rua) ##True
print(V1 and not V2 or V2 and not True) ##True
print(X > Y and C <= B) ##False
print(C - 3 * A < X + 2 * Z) ##True