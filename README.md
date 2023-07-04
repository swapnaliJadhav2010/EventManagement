# Event Management System
Create the Sport event management system where you can add,change,select and delete the data of sports, events and seletion tablethrough Rest API.

## Prerequisites:
Visual Studio code with python installation<br>
Postman<br>

### Installation:
Install Python and Django<br>
-sudo apt install python<br>
-python -m venv myenv<br>
-cd myenv\Scripts\activate (use .\activate)<br>

Verify installations:<br>
-python3 --version<br>

### Clone Repository
git clone <repository_url><br>
cd <repository_directory><br>
pip install -r requirements.txt<br>

### Run Django Project
Create the user to handle admin part<br>
python manage.py createsuperuser<br>

python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py runserver<br>

Your project will be running on http://127.0.0.1:8000<br>
Open this url in browser- http://127.0.0.1:8000/admin<br>
use the username and passowrd you created while creating the superuser<br>
click on '+ADD' in frony of Tokens , Then select user . This will create the Token(Note this token)

### Postman to Test the endpoint
Put the token in params 
![Token Insertion](<img width="503" alt="image" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/78864ea6-276c-448e-b840-7f7b5dde8c44">
)





