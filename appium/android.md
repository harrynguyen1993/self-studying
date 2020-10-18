#  Appium for Android
------------------------ 
## Setup
  - **Step 1: Install Appium using NPM**
    ===========================================
    - Commands to check if node and NPM are installed:
      - node -v
      - npm -v
    - Install node.js and NPM from link - https://nodejs.org/en/
    - Command to install Appium using npm: npm install -g appium
    - Command to start Appium: appium
    - Command to uninstall Appium: npm uninstall -g appium

 - **Step 2: Install Appium using Appium Desktop**
    ===========================================
    - Download and install Appium Desktop from https://appium.io


  - **Step 3: Install JAVA JDK and configure environment variable**
    ===========================================================
    - Command to check if JAVA is already installed: java -version
    - JAVA JDK download link: https://www.oracle.com/technetwork/ja...
    - JAVA 8 Installation instructions on Windows:
    https://docs.oracle.com/javase/8/docs...
    - Create JAVA_HOME system environment variable and set it to JDK path (without bin folder). 
    - Edit PATH system environment variable and add %JAVA_HOME%\bin


  - **Step 4: Install Android Studio and configure environment variable**
    =================================================================
    - Android Sutdio download link: https://developer.android.com/studio
    - Create ANDROID_HOME system environment variable and set it to SDK path. 
    - Edit PATH system environment variable and add below,
    %ANDROID_HOME%\platform-tools
    %ANDROID_HOME%\tools
    %ANDROID_HOME%\tools\bin
    %ANDROID_HOME%\emulator


  - **Step 5: Verify installation using appium-doctor**
    ===============================================
    - Command to install appium-doctor: npm install -g appium-doctor
    - Command to get appium-doctor help: appium-doctor --help
    - Command to check Android setup: appium-doctor --android 


  - **Step 6: Create AVD and start it [emulator setup]**
    ================================================
    - Open Android Studio
    - Click Configure option
    - Click "AVD Manager" option
    - Click "Create Virtual Device" button
    - Select the phone model
    - Download the Image for desired OS version if not already downloaded
    - Start AVD


  - **Step 7: Enable USB debugging on Android mobile [Real Device setup]**
    ==================================================================
    - On your phone,
    - Go to Settings
    - Click System option
    - Click "About Phone" option
    - Click on "Build Number" 7 to 8 times
    - Go back to Settings
    - Open Developer Options
    - Enable "USB Debugging"



------------------------
## Run and launch appication
- Capability to launch an application
 ```
  {
      "platformName": "Android",
    "platformVersion": "9.0",
    "deviceName": "Android_TV_API_28",
    "appActivity": "com.my.app.MainActivity",
    "automationName": "UiAutomator2",
    "app": "C:\\floware\\....Test_3.7.0_2008251655.apk",
    "appPackage": "com.vn.tv"
  }
 ```

- **1.1  Get list devices are on**
  - Open terminal and type command: adb devices

- **1.2	Get list name of emulator**
  - Open terminal and type command: emulator -list-avds

- **1.3	Get all app packages**
  - Open terminal and type command: adb shell pm list packages –f

- **1.4	Get appPackage and appActivity of current focus**
  - Open terminal and type command:  adb shell dumpsys window | find "mCurrentFocus"
  - Open emulator from command line
  - Open terminal and cd to emulator path
  - Cd C:\Users\Dell\AppData\Local\Android\Sdk\emulator
  - Type emulator -avd “_Android_TV_API_28” [Name emulator get from 1.2]
  
  
  
# Referent: 
  - https://support.testsigma.com/support/solutions/articles/32000019977-how-to-find-app-package-and-app-activity-of-your-android-app
  - https://www.toolsqa.com/mobile-automation/appium/appium-tutorial/
  - https://www.youtube.com/watch?v=MSp_pf4EgSg&ab_channel=SoftwareTestingMentor




