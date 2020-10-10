# Keyword Tip python

 - Enumerate
  ```
      import sys
      filename = sys.argv[1]
      with open(filename) as file:
          for index, line in enumerate(file):
          print("{0}: {1}".format(index+1, line), end='')
  ```
  - Swap params
  ```
    a,b = 10,11
    a,b =b,a
  ```

   - For one line params
  ```
    evens = [x for x in range(10) if x%2==0
    print(evens)
  ```

 ```
    list.map(function(), list_data)
    list.filter(function(), list_data)
    list.reduce(function(), list_data)
    list.map(lambda x: x*2, list_data)
    zip(list_a,list_b)
 ```