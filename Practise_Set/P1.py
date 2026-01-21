# Q. check the length of the string "Python is a case sensitive language"
string="Python is a case sensitive language"
print("Length of the string is:",len(string))

"""## 1️⃣ Python Basics (Used in Every Selenium Script)

### Variables & Input Handling
1. Store browser name (`"chrome"`, `"firefox"`) in a variable and print it.
2. Store URL of an application and print “Opening <URL>”.
3. Store username and password and print masked password (`******`).
4. Assign page title to a variable and print its length.
5. Store test environment (`QA`, `UAT`, `PROD`) and display which one is active.
6. Store timeout value (integer) and print `"Timeout set to X seconds"`.
7. Store execution result (`True/False`) and print pass/fail message.
8. Store error message text and print it in uppercase.
9. Store locator type (`"id"`, `"xpath"`) and locator value.
10. Swap two variable values (e.g., username & email). 

"""
#1
browser_name="chrome"
print("Browser name is:",browser_name)
#2
url="http://example.com"
print("Opening",url)
#3
username="user1"
password="mypassword"
masked_password="*" * len(password)
print("Username:",username) 
print("Password:",masked_password)
#4
page_title="Welcome to Example Application"
print("Length of the page title is:",len(page_title))
#5
test_environment="QA"
print("Active test environment is:",test_environment)
#6
timeout_value=30
print("Timeout set to",timeout_value,"seconds")
#7
execution_result=True
if execution_result:
    print("Test Passed")
else:
    print("Test Failed")
#8  
error_message="Invalid username or password"
print("Error message in uppercase:",error_message.upper())
#9
locator_type="id"
locator_value="usernameField"
print("Locator Type:",locator_type)
print("Locator Value:",locator_value)
#10
var1="username"
var2="email"
var1, var2 = var2, var1  #Swapping values
print("After swapping:")
print("var1:",var1)
print("var2:",var2)    