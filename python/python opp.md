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
    pass
 ```
  - Adding attributes to a class.
    ```
    >>> person = People()
    >>> person.name = "Harry"
    ```
  
    
