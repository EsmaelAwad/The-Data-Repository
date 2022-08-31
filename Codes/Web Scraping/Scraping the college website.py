from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import pandas as pd
import time
ids = pd.read_csv("Students IDs.csv",chunksize=5)
ress = []
try:
        
    try:
        
        for chunk in ids:
            
            chunk = chunk.sort_values(by="Student Id",ascending=True)
            
            for n in chunk['Student Id']:
                
                try:
                    
                    print(f"I am Scraping for {n}")
                    browser = webdriver.Edge()
                    browser.set_page_load_timeout(15)
                    try:
                        try:
                            st1 = time.time()
                            browser.get("http://app1.helwan.edu.eg/Commerce/HasasnUpMlist.asp")
                        
                            et1 = time.time()
                            el1 = et1-st1
                            print(f"Elapsed Time is: {el1} Seconds")
                            
                            
                            my_id = browser.find_element("name","x_st_settingno")
                            submitting = browser.find_element("name","Submit")
                            my_id.send_keys(n)
                            submitting.click()
                            if len(browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[8]/div/font/b').text)>0:
                                link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[9]/font/b/span/a')
                                time.sleep(0)
                                link_to_natega.click()
                            else:
                                link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[4]/td[9]/font/b/span/a')
                                time.sleep(0)
                                link_to_natega.click()
                        
                        
                            
                            name = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[3]/td[2]/div/font/b').text
                            result = browser.find_element("xpath",'/html/body/form/div/table[4]/tbody/tr[3]/td[3]/div/font').text
                            depa = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[5]/td[2]/div/font/b').text
                            if len(result)>0:
                                over = {name:[result,depa]}
                                ress.append(over)
                                print(f"i scraped{over}")
                            browser.quit()
                                    
                       
                        except TimeoutException as e:
                            print("Failed to get to website")
                            browser.refresh()
                            try:
                                try:
                                    print(f"I am refreshing for {n}")
                                    st1 = time.time()
                                    browser.get("http://app1.helwan.edu.eg/Commerce/HasasnUpMlist.asp")
                                
                                    et1 = time.time()
                                    el1 = et1-st1
                                    print(f"Elapsed Time is: {el1} Seconds")
                                    
                                    
                                    my_id = browser.find_element("name","x_st_settingno")
                                    submitting = browser.find_element("name","Submit")
                                    my_id.send_keys(n)
                                    submitting.click()
                                    if len(browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[8]/div/font/b').text)>0:
                                        link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[9]/font/b/span/a')
                                        time.sleep(0)
                                        link_to_natega.click()
                                    else:
                                        link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[4]/td[9]/font/b/span/a')
                                        time.sleep(0)
                                        link_to_natega.click()
                                
                                
                                    
                                    name = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[3]/td[2]/div/font/b').text
                                    result = browser.find_element("xpath",'/html/body/form/div/table[4]/tbody/tr[3]/td[3]/div/font').text
                                    depa = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[5]/td[2]/div/font/b').text
                                    if len(result)>0:
                                        over = {name:[result,depa]}
                                        ress.append(over)
                                        print(f"i scraped{over}")
                                    browser.quit()
                                            
                               
                                except TimeoutException as e:
                                    print("Failed to get to website")
                                    browser.refresh()
                                    
                            except NoSuchElementException as n:
                                print("Failed to get to website")
                                try:
                                    try:
                                        print(f"Timed out...refreshing for {n}")
                                        st1 = time.time()
                                        browser.get("http://app1.helwan.edu.eg/Commerce/HasasnUpMlist.asp")
                                    
                                        et1 = time.time()
                                        el1 = et1-st1
                                        print(f"Elapsed Time is: {el1} Seconds")
                                        
                                        try:
                                            
                                            my_id = browser.find_element("name","x_st_settingno")
                                            submitting = browser.find_element("name","Submit")
                                            my_id.send_keys(n)
                                            submitting.click()
                                            if len(browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[8]/div/font/b').text)>0:
                                                link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[3]/td[9]/font/b/span/a')
                                                time.sleep(0)
                                                link_to_natega.click()
                                            else:
                                                link_to_natega = browser.find_element("xpath",'//*[@id="ewlistmain"]/tbody/tr[4]/td[9]/font/b/span/a')
                                                time.sleep(0)
                                                link_to_natega.click()
                                        except NoSuchElementException as ee:
                                            print("failed to get to natega link")
                                    
                                        
                                        name = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[3]/td[2]/div/font/b').text
                                        result = browser.find_element("xpath",'/html/body/form/div/table[4]/tbody/tr[3]/td[3]/div/font').text
                                        depa = browser.find_element("xpath",'/html/body/form/div/table[1]/tbody/tr[5]/td[2]/div/font/b').text
                                        if len(result)>0:
                                            over = {name:[result,depa]}
                                            ress.append(over)
                                            print(f"i scraped{over}")
                                        browser.quit()
                                                
                                   
                                    except TimeoutException as e:
                                        print("Failed to get to website")
                                        browser.refresh()
                                        
                                except NoSuchElementException as n:
                                    print("Failed to get to website")
                                    browser.quit()
                                browser.quit()
                            
                    except NoSuchElementException as n:
                        print("Failed to get to website")
                        browser.quit()
                except TimeoutException as er:
                    continue
    except TypeError as t:
        print("Failed to get to website")

except WebDriverException as w:
    print("Failed to get to website")
print(ress)

import pandas as pd
df = pd.DataFrame()
f_d = []
department = []
df['names'] = [name for lis in ress for name in lis.keys()]
#print(df)
for item in ress:
    for val in item.values():
        f_d.append(val[0])
        department.append(val[1])
df['degree'] = f_d
df['department'] = department
df.to_excel("students.xlsx")