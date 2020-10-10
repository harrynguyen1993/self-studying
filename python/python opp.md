------------------------
#PYTHON : 
# Install python 
  - Download installer .exe in this link https://www.python.org/downloads/ (Windown)
  - Use command'brew install python3' - Mac moreover (check version 'pip --version' pip is a standard package manager used to install and maintain packages for Python )
  - Install libraries from txt file. 
    - pip install -r requirements.txt 
    - pip install "Name_library" 
    - pip list  [Check librarries have been installed] 
    - pip install --upgrade pip [We can upgrate other libraries by this commend]
    - pip -h [Help document]
------------------------
  
# 1. Object-oriented Design
  - Object-oriented analysis (OOA) is the process of looking at a problem, system, or task (that somebody wants to turn into an application) and identifying the objects and interactions between those objects. The analysis stage is all about what needs to be done.
The output of the analysis stage is a set of requirements. If we were to complete the analysis stage in one step, we would have turned a task, such as, I need a website, into a set of requirements
  - Object-oriented design (OOD) is the process of converting such requirements into an implementation specification. The designer must name the objects, define the behaviors, and formally specify which objects can activate specific behaviors on other objects. The design stage is all about how things should be done.
  - Object-oriented programming (OOP) is the process of converting this perfectly defined design into a working program
  - Unified Modeling Language( UML)The relationship between the four classes of objects in our inventory system can be described using a UML 
# 2. Creating Python classes
  ```
  class People:
    #pass
    def reset(self):
        self.name = ""
 ```
  - Adding attributes to a class.
    ```
    >>> harry = People()
    >>> harry.name = "Harry"
    >>> print f("Hello, My name is {harry.name}") # Hello, My name is Harry
    >>> harry.reset()
    >>> print(harry.name) # Name is ""
    ```
  - Contructor: Initializing the object
     ```
    class People:
      def __init__(self, name , address):
        '''Initialize the position of a new point. The x and ycoordinates can be specified. If they are not, the point defaults to the origin.'''
          self.name = name 
          self.address = address
      def reset(self):
          self.name = ""
     ```
# 3. Modules and packages
   
     ```
     import database
     db = database.Database()
      ----------
      from database import Database
      from database import *

      ```
    
# 4. When Objects Are Alike
     - Basic inheritance
     - Inheriting from built-ins
     - Multiple inheritance
     - Polymorphism and duck typing
  - Extending built-ins 
      ```
     dclass ContactList(list):
         def search(self, name):
            '''Return all contacts that contain the search value
            in their name.'''
            matching_contacts = []
            for contact in self:
                if name in contact.name:
                    matching_contacts.append(contact)
            return matching_contacts
    class Contact:
        all_contacts = ContactList()

        def __init__(self, name, email):
            self.name = name
            self.email = email
            self.all_contacts.append(self)
      ```
    - Overriding and super
      ```
      class Friend(Contact):
          def __init__(self, name, email, phone):
          super().__init__(name, email)
          self.phone = phone
      ```
  - Multiple inheritance and The diamond problem
     ```
          class Friend(Contact, AddressHolder):
             def __init__(
               self, name, email, phone,street, city, state, code):
               Contact.__init__(self, name, email)
               AddressHolder.__init__(self, street, city, state, code)
               self.phone = phone
          
          #  Here is the same code written using super
          class BaseClass:
              num_base_calls = 0
              def call_me(self):
                  print("Calling method on Base Class")
                  self.num_base_calls += 1
          class LeftSubclass(BaseClass):
              num_left_calls = 0
              def call_me(self):
                  super().call_me(self)
                  print("Calling method on Left Subclass")
                  self.num_left_calls += 1
          class RightSubclass(BaseClass):
              num_right_calls = 0
              def call_me(self):
                  super().call_me(self)
                  print("Calling method on Right Subclass")
                  self.num_right_calls += 1

          class Subclass(LeftSubclass, RightSubclass):
              num_sub_calls = 0
              def call_me(self):
                  LeftSubclass.call_me(self)
                  RightSubclass.call_me(self)
                  print("Calling method on Subclass")
                  self.num_sub_calls += 1
     ```
    
# 4. Expecting the Unexpected

  ```
    try:
      no_return()
    except:
       raise Exception(''Error exception)
       print("I caught an exception")
      print("executed after the exception")
  ```
  
   ```
   def funny_division2(anumber):
     try:
       if anumber == 13:
          raise ValueError("13 is an unlucky number")
       return 100 / anumber
     except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"
        
        
    for val in (0, "hello", 50.0, 13):
         print("Testing {}:".format(va
   ```
