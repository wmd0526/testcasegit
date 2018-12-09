from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_element=driver.find_element_by_id(id_="kw")
input_element.send_keys("软件测试")
button=driver.find_element_by_id(id_="su")
time.sleep(3)
button.click()
a_list=driver.find_elements_by_xpath(xpath='//div[@id="content_left"]//h3//a')

time.sleep(3)

print(len(a_list))

for item in a_list:
    print(item)
    print(item.text)
# for item in a_list:
#
#     if "软件测试" in str(item.text()):
#         print(True)

time.sleep(5)

# driver.quit()