# note-tap : https://pandao.github.io/editor.md/en.html, Editer
------------------------
#  Appium for Android
 
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
