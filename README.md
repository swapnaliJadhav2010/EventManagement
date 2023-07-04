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
Put the token in Headers as showen below:<br>
 <img width="503" alt="token" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/372d3e12-de76-40b7-8a24-eb3e9d3c3d05">
#### Test the Add functionality:
Test adding the sports, events and selection with json payload as shown :<br>
<img width="602" alt="createsport" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/3a7a3809-be7a-4211-8547-696392379856"><br>
<img width="587" alt="createevents" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/0b112cac-8831-475e-a7d5-d37b73dd3c0f"><br>
<img width="584" alt="createselection" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/cffc9ad5-72d7-4a14-a616-a03bd2e7b70c"><br>

#### Test the update functionality:
you need to use the id of the instance you want to change :<br>
<img width="582" alt="updatesport" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/746aebd7-d0bf-4b52-98a8-fa24373c8200"><br>
<img width="581" alt="updateevents" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/e07f8613-9355-4255-ac09-7e13380f7dd7"><br>
<img width="590" alt="updateSelection" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/6ec6237c-93bb-430f-b2c3-6202529d3a59"><br>

#### Test the filter functionality:
check the events available for particular sport:<br>
<img width="597" alt="filterBySportName" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/c6d6feda-2f3f-478e-9170-f3a71755197b"><br>
check the selections available for particular event<br>
<img width="593" alt="filterByEventName" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/2d2d076f-778b-4d0d-9a8b-754d40f79d51"><br>
check the price in the range<br>
<img width="587" alt="filterByPrice" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/d217aa3c-6f04-4dde-a150-583bbadbb90a">

### Test the delete functionality:
use sport id to delete it:<br>
<img width="593" alt="deletesport" src="https://github.com/swapnaliJadhav2010/EventManagement/assets/126250475/c29df915-a5a3-4224-8189-5b08598c2570"><br>
you can delete the events and selections in same way
















