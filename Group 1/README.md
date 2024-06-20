# Demo #
## See JFCSoftwareDemo,Demo2,Demo3 ## 
### for a quickly understand of ### 
### how this system working ###
### and basic operating principles and processes ###

# Current Issues #
1. Can not keep the website interface(typical audio name in practice page and current list in teaching dashboard) 
   updating to all the things after each edit or remove actions
    Maybe caused by asyc issues?
2. When add-in new audio data, cannot be repeated with the existing ones in the audio library.
3. Need to be able to automatically change to the new list we created
4. 'active' should be changed to another word, also the icon
5. diff current list have different active sounds, make a choice for selecting diff list in practice page
6. getActiveHeartAudio and getActiveLungAudio
7. 'Active' icon needs to be explained
8. Current list should not change after change page, eg. from teaching dashboard to practice page and change back
9. There should be a current list instruction on the practice page
10. Bug - there are multiple lists that has activated audio
11. How to handel very long list?
12. NOoooo
12. NOoooo?



# Solved Issues #

1. rename and remove too similar to each other --- delete list
2. help page still need imporve with icon
3. bigger icons for heart and lungs
4. switch the position of audio library and current list
5. use different color rather than orange
6. list saving (creating or updating)
7. Attention: no list content cleaning after remove the list
8. No list can have the same name
9. mounted of style in Help Page
10. sorting mechnithm for heartand lungs
11. searching bar will be good
12. CRUD for the audio content (interface design)
13. When cancel the add new list action, a default listX is still added
14. Audio edit dialog (backend database saving action)
15. Link will expire and local storage needed...
16. Time needed before active audio are ready to play (preloading? or Local database?)
17. After we have local storage, browse and import audio function is needed
18. can't edit the audio name in the edit mode
19. Add mode cant deal with file uploading
20. When adding new audio data, you need to provide all the information (excluding description)
21. sovled with optimized delete list content accordingly: Removing a audio from audio library may trigger some bug when I have added a lot of audio to one or more current lists

# !!!ATTENTION!!! #
## Each time after ##
```
  git pull
```
### Frontend ###
Run
```
  npm install
  npm run dev
```
### Backend ###
Run for normal situations:
```
  python manage.py migrate

  python manage.py runserver
```
#### OR ####
Run when database updating needed:
```
  python manage.py deleteAll
  python manage.py migrate
  python manage.py initialDb

  python manage.py runserver
```
# Good Luck & Have Fun! #
## --------------------Readme starts here----------------------- ##
# AMOD || Auscultation Model of Dog #
## This is the application for the JFC Group 14 - Dog Auscaltation Model. ##
### Start from 1st Dec, 2023 ###
### Expect to finish at 9th Feb, 2024 ###
## The objectives are: ##
    A user interface
    Process signal that comes from the hardware part
    Store the simulation sound sent to the model
    Send properly the audio to the model through the BLE
    Help the student to identify a abnormal sound
    Train the student to count the heatbeat
Updated 20231201

# Initialization #
## Frontend ##
  You need python for the following int
  pip install node (download the node.js from the web is more recommended)
  pip install npm (best using the admin mode)
  npm install (update the packages inside of ausfront folder)
  then 
  npm run dev
## Backend ##
  python manage.py migrate
  python manage.py initialDb
  python manage.py runserver


# Frontend - vue3 + Vite #
## Creating: ##
PS D:\Group14JFC\aus> npm create vue@latest
Need to install the following packages:
create-vue@3.8.0
Ok to proceed? (y) y

Vue.js - The Progressive JavaScript Framework

√ Project name: ... ausfront
√ Add TypeScript? ... Yes
√ Add JSX Support? ... Yes
√ Add Vue Router for Single Page Application development? ... Yes
√ Add Pinia for state management? ... Yes
√ Add Vitest for Unit Testing? ... Yes
√ Add an End-to-End Testing Solution? » No
√ Add ESLint for code quality? ... Yes
√ Add Prettier for code formatting? ... Yes

Scaffolding project in D:\Group14JFC\aus\ausfront...

Done. Now run:

  cd ausfront
  npm install
  npm run format
  npm run dev

# Recommend Tools #

BootStrap
FontAwesome
Rest_framework

# Backend - Django #
django-admin startproject ausback
cd ausback
python manage.py startapp aus
+ management/commands
+ static/.csv
+ installed_apps...
  rest_frameworks and cors

# Key Words #
### Vue 3 ###
  Framework for frontend development
### Vite ###
  Build Tools for automatically application build
### Vuex ###
  Official status management library (store)
### ESLint ###
  Javascript code inspection and repair tool
### Prettier ###
  Code formatting tools
### Element plus ###
  Component library, providing rich UI components and styles
### Gdurl.com ###
  For creating link to view or download the files on Google Drive
