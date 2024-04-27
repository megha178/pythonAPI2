#python API Automation framework

#integration test cases for the restful booker

URL - https://restful-booker.herokuapp.com/apidoc/
Auth - basic auth, cookie based
verify get,post,patch,delete
response,body,headers,status code

tech stack
1. request module
2. pytest , pytest-html,
3. allure report
4. Faker,csv,json
5. run via commandline - jenkins

# how to run via jenkins:

install pip packages:
 pip install pytest requests pytest-html faker allure-pytest jsonschema
pip is used to install the dependecies

run test folder:
pytest tests/* - s -v --alluredir=./reports --html-report.html

 pytest test_createbooking.py -s -v --alluredir=./reports --html=report.html


