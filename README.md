# PythonTest

Test Suites Project.

This project contains a set of test suites written in Python. Test Scripts were written in order to  complete the Task.
Test Suites:
1.	API_Testing: Contains tests for API endpoints [Task 3].
2.	EPAMcom: Contains tests related to [Task 1].
3.	e-shop: Contains tests related to [Task 2].
________________________________________
Installation.

The project requires Python 3.12 or above and uses pytest as the testing framework.
1.	Clone the Project:
git clone https://github.com/MaksGrynk00/PythonTests
2.	Set up a virtual environment (optional but recommended):
python3 -m venv venv
3.	Install required dependencies: You will find a requirements.txt file in the root directory. Install the dependencies required for this project by running:
pip install -r requirements.txt
________________________________________
Requirements:

This project requires the following dependencies listed in requirements.txt:

________________________________________
Running Tests.

To run the tests, navigate to the root directory of the project and run the following command:
python -m pytest <folder name>
folder_name  - replace with correct folder name if you want to run specific tests

To run one single test, navigate to the root directory of the project and run the following command:
python -m pytest <test name>
________________________________________
Execute test Suites. 

** Suite API_Testing: 
Test Suite include test scripts want could be executed in Pytest or command line and cover use cases from  Scope.
1) Scope: Create API tests for the following scenarios:
Use public API Swagger for Pets Store >> https://petstore.swagger.io/#/ 

•	Verify that allows creating a User
•	Verify that allows login as a User
•	Verify that allows creating the list of Users
•	Verify that allows Log out User
•	Verify that allows adding a new Pet
•	Verify that allows updating Pet’s image
•	Verify that allows updating Pet’s name and status
•	Verify that allows deleting Pet 

2) Fixtures in API Testing
This section documents the fixtures available in the conftest.py file for your API testing suite:
API Endpoints:
•	api_url1: Provides the base URL for the test "login User" endpoint: "https://petstore.swagger.io/v2/user/login".
•	api_url2: Provides the base URL for the "create User" endpoint: "https://petstore.swagger.io/v2/user".
•	api_url3: Provides the base URL for the "create pet" endpoint: "https://petstore.swagger.io/v2/pet".
•	api_url4: Provides the base URL for the "create user list" endpoint: "https://petstore.swagger.io/v2/user/createWithArray".
•	api_url5: Provides the base URL for the "update pet" endpoint: "https://petstore.swagger.io/v2/pet".
•	api_url6: Provides the base URL for the "pet image" endpoint: "https://petstore.swagger.io/v2/pet/444/uploadImage".
•	api_url7: Provides the base URL for the "delete pet" endpoint: "https://petstore.swagger.io/v2/pet".
•	api_url8: Provides the base URL for the "User logout" endpoint: "https://petstore.swagger.io/v2/user/logout".
Data Fixtures:
•	login_credentials: Provides a dictionary containing username and password for login tests: { "username": "UI0000123", "password": "UI0000123" }.
•	user_data: Provides a dictionary containing user data for creating users: Includes id, username, personal details, and userStatus.
•	new_pet_data: Provides a dictionary containing new pet data for creation: Includes id, category, name, photoUrls, tags, and status.
•	user_list: Provides a list with user data for creating multiple users: Each list item is a dictionary with user information.
•	updated_pet_data: Provides a dictionary containing updated pet data: Includes the same structure as new_pet_data with modified values for specific fields.
•	image_path: Provides the path to an image file for the "pet image" upload test (replace with your actual image path).
•	pet_id: Provides the ID of a pet to be deleted during testing (replace with the actual ID you want to delete).

** Suite e-shop: 
Test Suite include test scripts want could be executed in Pytest or command line and cover use cases from  Scope.
* Scope: Use public e-shop site >> https://demowebshop.tricentis.com/

--	Verify that allows register a User
--	Verify that allows login a User
--	Verify that ‘Computers’ group has 3 sub-groups with correct names
--	Verify that allows sorting items (different options)
--	Verify that allows changing number of items on page
--	Verify that allows adding an item to the Wishlist
--	Verify that allows adding an item to the card
--	Verify that allows removing an item from the card
--	Verify that allows checkout an item 

* Fixtures in e-shop: 
This section describes the fixtures provided in the conftest.py file used for test setup in your EPAM.com or E-Shop test folders.
Browser Fixture:
browser (session scope): Provides a WebDriver instance for interacting with the browser. This fixture utilizes the appropriate browser driver. Currently fixture configured for Firefox browser driver to change browser please configure file with comments for Chrome driver.
Example: 

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

** Suite EPAMcom: 

* Scope: 
   Test for scenario.
1) Check the title is correct
Steps
Open EPAM.com
Compare the title 
The title should be equal "
'EPAM | Software Engineering & Product Development Services'"
 
2) Check the ability to switch Light / Dark mode
Steps
Open EPAM.com
Switch the toggle for theme to opposite state
Expected: the theme should be changed to opposite
 
3) Check that allow to change language to UA
Steps
Open EPAM.com
Switch the site's language to Ukraine
Expected: The site's context should be changed to UA
 
4) Check the policies list
Steps
Open EPAM.com
Go to the bottom of the page
Check the policies list
Expected: The policies list should include the following items: 
INVESTORS
COOKIE POLICY
OPEN SOURCE
APPLICANT PRIVACY NOTICE
PRIVACY POLICY
WEB ACCESSIBILITY
 
5) Check that allow to switch location list by region
Steps
Open EPAM.com 
Go to Our Locations part
Check that 3 regions are presented [AMERICAS, EMEA, APAC] and allows to switch the region's locations list
 
6) Check the search function
Steps
Open EPAM.com
Open search field and submit request "AI"
Expected:  the site should show the search result
 
7)  Chack form's fields validation
Steps
Open https://www.epam.com/about/who-we-are/contact
Check validation for required fields
Expected: Required fields 
 
8) Check tha the Company logo on the header lead to the main page
Steps
Open https://www.epam.com/about
Click on the company logon on the header
Expected: https://www.epam.com/ page should be opened
 
9) Check that allows to download report.

* Steps
Open https://www.epam.com/about
Download EPAM Corporate Overview 2023 report on "EPAM at
a Glance" block
Expected: The files should be downloaded and have corect name and extension

* Fixtures in EPAM.com Testing
This section documents the fixtures provided in the conftest.py file for your EPAM.com test suite.
Browser Fixture:
--	browser: Provides a WebDriver instance for interacting with the EPAM.com website. This fixture uses Firefox by default (you can uncomment the Chrome driver line if preferred). It also sets the browser window size to 1200x800 for consistent test execution. The fixture yields the WebDriver instance and handles quitting the browser after each test.
URL Fixture:
--	url1 (params fixture): Provides the URL for your EPAM.com tests. It currently uses a single parameter https://www.epam.com. You can modify this to include additional URLs if needed.
Test Data Fixtures:
--	expected_policy (function scope): Supplies expected policy text for multiple tests (identified by test1-4 and test1-5 presumably). This fixture is defined twice in the current conftest.py, but it's recommended to consolidate it into a single fixture with appropriate test-specific data as parameters.
Download Directory Fixture:
--	get_download_dir: Provides the path to the user's Downloads directory for potential download-related tests. This leverages the os module to obtain the appropriate path based on the user's operating system.
By utilizing these fixtures, you can achieve more maintainable and flexible test code, ensuring consistent setup and data access for your EPAM.com tests.
