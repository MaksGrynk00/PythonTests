from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get("https://www.epam.com")
    assert chrome.title == "EPAM | Software Engineering & Product Development Services", "Title does not match"
    print('Test passed successfully')

except Exception as e:
    print('Test Failed. Reason:', str(e))
    
finally:
    chrome.quit()