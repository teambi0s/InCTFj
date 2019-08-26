# Challenge Name : T3

### Challenge File : [T3.apk](Handout/T3.apk)

# Description 
Oh I forgot to hide a debugging information  when I generated this apk. Can you check weather its visible?

Flag format : inctfj{}



# Flag
inctfj{Th15_15_ju5t_th4_b3g1nn1ng}


# How to Solve it

First you need to install ADB (Android Debugging Bridge ) on your computer and  enable USB debugging on your Android device ,this is to provide  access of your device to ADB.Once it’s done ,connect your Android device to your computer and start the app. Meanwhile run “ adb logcat | grep inctfj”. Win a game to get the flag in ADB.

