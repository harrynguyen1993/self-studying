#  Types of Selenium Waits For Page Load
------------------------ 
## When performing automation testing with Selenium, we use the following types of waits as we generate our Selenium script:
    - Thread.Sleep() method
    - Implicit Wait
    - Explicit Wait
    - Fluent Wait

## Thread.Sleep()
    - Stop the execution of the script for the specified duration of time
    - Thread.sleep(3000);
## Implicit Wait
    - It is by default applied to all the elements in the script.
    - driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
    - Implicit wait is that it is applied globally
## Explicit Wait
    - The Explicit wait is another one of the dynamic Selenium wait
    - WebDriverWait wait = new WebDriverWait(driver,30);
    - wait.until(ExpectedConditions.visibilityOfElementLocated(Reference of Element to be  located using locator));
    ```
    Types of Expected Conditions: Below are the few types of expected conditions commonly used as you perform automation testing with Selenium.

        - visibilityOfElementLocated()- Verifies if the given element is present or not
        - alertIsPresent()- Verifies if the alert is present or not.
        - elementToBeClickable()- Verifies if the given element is present/clickable on the screen
        - textToBePresentInElement()- Verifies the given element have the required text or not
        - titlels()- Verify the condition wait for a page that has a given title
    ```
## Fluent Wait
    - The Fluent wait is similar to explicit wait in terms of its functioning.

    ```
    Wait<WebDriver> fluentWait = new FluentWait<WebDriver>(driver)
       .withTimeout(60, SECONDS) // this defines the total amount of time to wait for
       .pollingEvery(2, SECONDS) // this defines the polling frequency
       .ignoring(NoSuchElementException.class); // this defines the exception to ignore 
      WebElement foo = fluentWait.until(new Function<WebDriver, WebElement>() {
     public WebElement apply(WebDriver driver)  //in this method defined your own subjected conditions for which we need to wait for
     {  return driver.findElement(By.id("foo"));
    }});
    ```

    ```
    Wait wait = new FluentWait(WebDriver reference)
    .withTimeout(timeout, SECONDS)
    .pollingEvery(timeout, SECONDS)
    .ignoring(Exception.class);

    WebElement foo=wait.until(new Function<WebDriver, WebElement>() {
    public WebElement applyy(WebDriver driver) {
    return driver.findElement(By.id("foo"));
    }
    });
    ```