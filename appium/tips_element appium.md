# Appium find element
  - Accessibility ID
  - Class name
  - ID	- resource-id 
  - Name	
  - XPath


  ## XPath
  ```
    - contains()
      - Xpath=//*[contains(@type,'sub')]  
      - Xpath=//*[contains(@type,'sub')]  
      - Xpath=//*[contains(@name,'btn')]

    - Using OR & AND:
      - Xpath=//*[@type='submit' or @name='btnReset']
      - Xpath=//input[@type='submit' and @name='btnLogin']

    - Xpath Starts-with
      - Xpath=//label[starts-with(@id,'message')]
    
    - XPath Text() Function
      - Following
        - Xpath=//td[text()='UserID']	

    - XPath axes methods
      - Xpath=//*[@type='text']//following::input[1]
```