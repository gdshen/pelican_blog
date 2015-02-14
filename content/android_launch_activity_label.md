Title:Android应用名与launch activity的名字的关系
Date:February 13, 2015 3:05 PM
Category:Android
Tags:Android, UI

# 将android应用的名字更改为与主activity不同
```xml
<activity
    android:name=".MainActivity_"
    android:label="@string/title_activity_main" >
    <intent-filter android:label="@string/app_name">
        <action android:name="android.intent.action.MAIN" />
         <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```
`<intent-filter android:label="@string/app_name>`中进行设置