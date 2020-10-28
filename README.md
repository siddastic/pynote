# PyNote
Pure Python Notes App

## Installing

Make sure you have the latest version of Python and **Tkinter**

## Running

In Project root directory **Execute** :
```
python app.py
```

## File Structure

Its mostly a mess currently 😅
But lemme try to explain
* AppData - stores all your notes and is dynamically created at first run
* Design - contains files related to app UI
    * clean.py - stores all *packed* objects to *pack_foget* to clear screen
    * fullscreen.py - stores function to make app fullscreen
* partials - create mixed mess of tkinter screens (collection of objects packed as a screen) and login file
    * editSceen.py - Note Editing Screen
    * fileManager.py - All Note Reading and creation related operations
    * firstScreen.py - That Splash Screen Animation
    * secondScreen.py - Wall Screen for all your Notes
* Settings - settings for your app
    * collection.json - just stores boolean value of you DarkMode state 😅
* **app.py** - Not Much Code here but manages all screens and responsible for App KickStart!

Rest you know those Liscense and readme stuff.... Formalities.... (fooooo)