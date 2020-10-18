# Appium Desktop iOS

## Installing XCode
  - Xcode installed
## Installing Homebrew and Carthage
  - Homebrew 2.4.3+ installed
    - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    -  brew -v
  - Carthage
    - brew install carthage
## Installing JDK
  - Install jdk and Set JAVA_HOME 
    - Open ~/.bash_profile with a text editor and add the line export JAVA_HOME=$(/usr/libexec/java_home. Save the file and run source ~/.bash_profile from the terminal
## Installing Appium  
  -  Appium Server 1.17.1+ installed via Node
    - npm install appium -g
    - (In case we have an issue related to permission denied, try this: sudo npm install -g appium --unsafe-perm=true --allow-root )
    -  appium -v
  - Appium Desktop 1.17.1-1+ installed
  - Appium-doctor
    - npm install -g appium-doctor
## Setting up the Environment for iOS Testing on Real Device
  - Install Required dependencies for real devices
    ```
    - brew install libimobiledevice --HEAD
    - brew install ios-deploy
    - npm install -g authorize-ios
    - brew install ideviceinstaller
    - brew install ios-webkit-debug-proxy
    ```
  - Prepare Signing Certificate and Provisioning Profile
  ```
   - Open Xcode
   - Go to Xcode -> Preferences...
   - Click the Accounts tab
   - Click the + button to add an account
   - Select Apple ID as the account type and click Continue
   - Enter your Apple ID and password
  ```
## Build WebDriverAgent
  - For Appium Desktop Users:
    ```
      >>> cd /Applications/Appium.app/Contents/Resources/app/node_modules/appium-webdriveragent

      >>> ./Scripts/bootstrap.sh –d

      >>> mkdir -p Resources/WebDriverAgent.bundle
    ```
  - For Appium Desktop Users:
    ```
      >>> /usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent

      >>> ./Scripts/bootstrap.sh –d

      >>> mkdir -p Resources/WebDriverAgent.bundle
    ```
## Open WebDriverAgent.xcodeproj in Xcode 
  ```
    - Select WebDriverAgent > WebDriverAgentRunner.
    - Deselect the Automatically manage signing checkbox.
    - Under provisioning profile > select the example_Provision.mobileprovision file that you prepared earlier.
    - On the menubar, select Product > build
  ```

## Run and launch appication
- Capability to launch an application
  ```
    {
    "platformName": "iOS",
    "platformVersion": "13.1",
    "deviceName": "iPhone 11 Pro Max",
    "automationName": "XCUITest",
    "app": "C:\\floware\\....Test_3.7.0_2008251655.ipa",
    "udid": "<udid of real device>"
    }
  ```
# Refer
  - http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/
  - https://docs.gondolatest.com/mobile-testing-guide/setup-ios-environment.html#prerequisites
  - https://www.youtube.com/watch?v=-_6C_-CMqSk&t=1691s&ab_channel=AutomationStepbyStep-RaghavPal