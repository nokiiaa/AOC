class file:
  def __init__(self, sz, name, parent):
    self._size = sz
    self.name = name
    self.parent = parent
  def size(self):
    return self._size

class directory:
  def __init__(self, name, parent=None):
    self.parent = parent
    self.name = name
    self.children = []
  def find_child(self, c):
    return [-1, *(i for i, x in enumerate(self.children) if x.name == c.name and str(type(x)) == str(type(c)))][-1]
  def size(self):
    return sum(x.size() for x in self.children)

def day7(data):
  i = 0
  cd = root = directory('/')
  data = data.splitlines()
  while i < len(data):
    l = data[i]
    if l.startswith('$ cd'):
      d = l.split(' cd ')[1]
      if d == '..':
        cd = cd.parent
      elif d == '/':
        cd = root
      else:
        new_dir = directory(d, cd)
        f = cd.find_child(new_dir)
        if f == -1:
          cd.children.append(new_dir)
        else:
          new_dir = cd.children[f]
        cd = new_dir
    elif l.startswith('$ ls'):
      while i+1 < len(data) and data[i+1][0] != '$':
        i += 1
        a, b = data[i].split(' ')
        c = file(int(a), b, cd) if a.isdigit() else directory(b, cd)
        if cd.find_child(c) == -1:
          cd.children.append(c)
    i += 1
  sizes = []
  def walk(d):
    sizes.append(d.size())
    for c in d.children:
      if isinstance(c, directory):
        walk(c)
  walk(root)
  p1 = sum(filter(lambda x: x < 1e5, sizes))
  p2 = next(filter(lambda x: x >= root.size() - 4e7, sorted(sizes)))
  return p1, p2