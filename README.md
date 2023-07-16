# NAVIKONLINE
# Steps to run the project
1. Install package using command 'pip install virtualenvwrapper-win'
2. Create a Virtual Environment with command 'mkvirtualenv env_name'
3. Install all the requirements in your virtual environment using command 'pip install -r requirements.txt'

# You can Get Private and Public API Keys from accountsettings of builder.io
Click and Login: https://builder.io/account/space
Go to following location and get API Keys
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/dfd20e31-cec6-4601-a276-cc5677c327d9)


# Settings.py
# Give your Builder API Key here
- BUILDER_API_KEY = 'Your Private APIKey'
- BUILDER_PUBLIC_KEY = 'Your Public APIKey'
- BUILDER_AUTO_CREATE_PAGES = True

# Inside reactappbuilder folder
# Give your Public API Key
# App.js
builder.init('Your API Key Here');

# Create a Page in Your Builder.io as shown in Image inside youe builder workspace.
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/5b05ca62-07a3-4b1f-9df1-f6138807cd33)

# Create Model and set preview url in builder.io as shown in Image
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/bb98ebcf-f33d-4c67-bfaa-f01ab0337156)

# Go to reactapp using cd and install node modules
- npm install
- 
# and then give build command
npm run build
# check whether react app is running at port 3000 using 
- npm start

# Then run django server by command at port 8000
python manage.py runserver

# Open your page in builder.io
I am facing the following errors in builder page and react app displays blank page.
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/f47b61d8-4e61-45a3-ab5b-797fee3e0c0d)
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/0e0d07b2-0ce1-4d6c-8867-16659593ef96)
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/efc9c645-97e0-4f8f-be92-5203755b12e6)
![image](https://github.com/vknan/Vijay_Portfolio/assets/70138450/34892026-fdeb-44b0-b1ca-968ffd1a4f34)

# Note:
- Keep the django server running to test builder.io integration


