def hello():
    print("Hello, this is a greeting to the user!")


def pack(a, b, c):
    list = [a, b, c]
    print(list)

def packs(a, b, c):
    return [a, b, c]


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")



# functions invoking:
hello()
print(pack('dog', 'cat', 'fish'))
print(packs('squirell', 'lion', 'tiger'))
eat_lunch([])
eat_lunch(['fish sandwich'])
eat_lunch(["apple", "banana", "orange", "kiwi"])