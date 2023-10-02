# Lista en una función
# Rosa Herrera - ESIT

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s

print(list_sum([5, 4, 3]))

#print(list_sum(5))   error, ya que no puede iterar solo un número
