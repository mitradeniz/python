
a = 0
b = 1
x = [3,6,8,4,3243253,464567456345,345323,32435346457568,34564,1,-324]
t = list(x)
f = len(x)
g = len(t) 

def find_bigger():
  f = len(x)

  while f >= 2:
    m = x[a]
    l = x[b]
    if m > l:
      x.remove(x[b])
      
      f -= 1
    else:
      x.remove(x[a])
      
      f -= 1
  print("Biggest number: ", x[a])
def find_smaller ():
  g = len(t) 

  while g >= 2:
    y = t[a]
    u = t[b]
    if y > u:
      t.remove(t[a])
      g -= 1

    else:
      t.remove(t[b])
      g -= 1

  print("Smallest number: ", t[a])
