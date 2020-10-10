# *args and **kwargs in Python
------------------------
## *args (Non-Keyword Arguments)

## **kwargs (Keyword Arguments)


------------------------
```
# *args 
  def myFun(arg1, *argv):
      print ("First argument :", arg1)
      for arg in argv:
          print("Next argument through *argv :", arg)
  
  myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
  -------------------
  Output
    First argument : Hello
    Next argument through *argv : Welcome
    Next argument through *argv : to
    Next argument through *argv : GeeksforGeeks

```


```
# ***kwargs 
## Python program to illustrate  
## *kargs for variable number of keyword arguments
 
    def myFun(**kwargs): 
        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))
 
  ## Driver code
  myFun(first ='Geeks', mid ='for', last='Geeks')    
  -------------------
  Output
    First argument : Hello
    Next argument through *argv : Welcome
    Next argument through *argv : to
    Next argument through *argv : GeeksforGeeks

```