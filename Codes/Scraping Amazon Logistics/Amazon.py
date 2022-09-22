import time
import pandas as pd
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt

'''
In this script, for simplicity, to avoid the StaleElement Error, instead of
using these methods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

we will just wait for the page to:
    1- Destroy the element we are looking for
    2- reconstruct the element we are looking for

using the time.sleep(3) method.

other methods could have been used, but for the code to be more readable, we use this simple method.
'''


'''
In this script, Anything that needs you to supply manually is denoted by:
    #______----------------_____-----------____
    Things you need to fill:
        1-username
        2-password
        3-station to scrape data for
        4-date to scrape data for
'''
#functions to get the dates for the calendar.
today = dt.today()
today_day = today.strftime('%d')
today_month = today.strftime('%B')

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://logistics.amazon.eg/account-management/")
user = driver.find_element("xpath",'//*[@id="ap_email"]') 
password = driver.find_element("xpath",'//*[@id="ap_password"]')
user.send_keys("insert your username") #______----------------_____-----------____
password.send_keys("inseert your password") #______----------------_____-----------____
login = driver.find_element("xpath",'//*[@id="signInSubmit"]').click()

#up until here, We are in the home tab
#here, we coose specific tap which is operations.
def press_operations():
    operations = driver.find_element("xpath",'//*[@id="fp-nav-menu"]/ul/li[4]/a').click()
    delivery = driver.find_element("xpath",'//*[@id="fp-nav-menu"]/ul/li[4]/ul/li[1]/a').click()

press_operations()

#This "Choose" is to be able to write the station's name.
def click_choose():
    choose = driver.find_element("xpath",'//*[@id="main"]/div/div/div[1]/div[1]/div/div/div[2]/span').click()

click_choose()

def get_station(st):
    #Find the search for the station desired
    driver.find_element("xpath",'//*[@id="main"]/div/div/div[1]/div[1]/div/div[2]/div[1]/input').send_keys(f"{st}")
    time.sleep(5)
    if st=="DAI3":
        driver.find_element("xpath",'//*[@id="s5d3cdbae-d1d6-47f4-8606-ba55c03981d4"]').click()
    elif st=="DAI4":
        driver.find_element("xpath",'//*[@id="s7830c83d-bf86-4976-a6e1-2725123a833a"]').click()
    elif st=="DGI7":
        driver.find_element("xpath",'//*[@id="s1b523eb7-341e-4f3f-920d-2bf4ebb292f6"]').click()
        
#Now we are in the performance page of the selected Station.

get_station("DGI7") #______----------------_____-----------____

#Let's scrape whatever we can


def get_date(month=today_month,day=today_day,year=2022):
    ''' This function will choose the date from
        the calendar object in the website,
        If no date is satisfied at all it will
        scraape todays date.
    '''
    try:
        #Find The calendar Element
        driver.find_element("xpath",'//*[@id="main"]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/i').click()
        driver.find_element(By.CSS_SELECTOR,f'[aria-label="{month} {day}, 2022"]').click()
    except:
        print("Day selected must be less than today's date by 14 days\n",
              f"Today's Date is {dt.today()}, Which I am now showing Data for")

#Up till now, testing for choosing the date for which i want to scrape the data works fine        

get_date(day=16) #______----------------_____-----------____
time.sleep(5)

#Now that we chose the date we want to scrape infrmation about, Let's click some links!
IDs = driver.find_elements(By.CSS_SELECTOR,'[class="text-muted-darker text-sm mr-1"]')
names = driver.find_elements(By.CSS_SELECTOR,'[class="transporter-name font-weight-bold pr-2 text-truncate"]')
stops = driver.find_elements(By.CSS_SELECTOR,'[class="d-flex justify-content-between"]')

driver_id = []
driver_name = []
stop_amount = []
stops_target = []
for d in IDs:
    dd = d.text
    driver_id.append(dd)

for d in names:
    dd = d.text
    driver_name.append(dd)
    
for d in stops:
    dd = d.text
    stop_amount.append(dd[0:2])

for d in stops:
    dd = d.text
    stops_target.append(dd[3:5])
    
df= pd.DataFrame()

df['name'] = driver_name
df['driver id'] = driver_id
df['stops delivered'] = stop_amount
df['stops target'] = stops_target


scraped_date = driver.find_element(By.CSS_SELECTOR,'[class="cortex-calendar-selection d-flex cursor-pointer border"]').text
scraped_branch = driver.find_element(By.CSS_SELECTOR,'[class="af-dropdown"]').text
day = scraped_date[:2]
mon = scraped_date[3:5]
year = scraped_date[6:]

df['Date'] = scraped_date
df['Branch'] = scraped_branch
df.drop_duplicates(subset=['name'])
df.to_excel(f"Attendance Output ({day}-{mon}-{year}) for {scraped_branch}.xlsx",index=False)

#I'll try to improve the logic!
driver_name = []
driver_id = []
driver_stops = []
driver_picks = []
driver_delivery = []
first_orders = []
last_orders = []

for dd in df['driver id']:
    for i in range(10):
        try:
            try:
                driver.get("https://logistics.amazon.eg/account-management/")
                time.sleep(3)
                press_operations()
                time.sleep(3)
                click_choose()
                time.sleep(3)
                get_station("DGI7") #______----------------_____-----------____
                get_date(day=16) #______----------------_____-----------____
                time.sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/span/div/div/div/div[2]/div/input').click()
                time.sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/span/div/div/div/div[2]/div/input').send_keys(dd)
                time.sleep(3)
                driver.find_element(By.CSS_SELECTOR,'[class="af-link link-to-content-selectable "]').click()
                time.sleep(3)
                
                #getting the Name
                name = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div')
                driver_name.append(name.text)
                
                #getting the id
                driver_id.append(dd)
                
                #getting stops
                stops = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/span')
                driver_stops.append(stops.text)
                
                #getting picks
                picks = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[4]/span')
                driver_picks.append(picks.text)
                
                #getting Deliveries
                delivery = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[5]/span')
                driver_delivery.append(delivery.text)
                try:
                    links = driver.find_elements(By.CSS_SELECTOR,'[class="af-badge positive"]')
                    if links[0].text[:9] == "Delivered":
                        
                        links[0].click()
                        time.sleep(3)
                        first_order_time = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div').text
                        time.sleep(3)
                        go_back = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/a/div/i').click()
                        time.sleep(3)
                    else:
                        links[1].click()
                        time.sleep(3)
                        first_order_time = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div').text
                        time.sleep(3)
                        go_back = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/a/div/i').click()
                        time.sleep(3)
                        
                    links = driver.find_elements(By.CSS_SELECTOR,'[class="af-badge positive"]')
                    if links[-1].text[:9] == "Delivered":
                        
                        links[-1].click()
                        time.sleep(3)
                        last_order_time = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div').text
                    else:
                        links[-2].click()
                        time.sleep(3)
                        last_order_time = driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div').text
                    first_orders.append(first_order_time)
                    last_orders.append(last_order_time)
                    print(first_order_time)
                    print(last_order_time)
                except:
                    first_orders.append("Not Available")
                    last_orders.append("Not Available")
            except:
                print(f"Failed to get data for {dd}")
        except:
            print(f"retrying for the {att+1}th time")
        else:
            break

            
df_detailed = pd.DataFrame({"Driver Name":driver_name,\
                            "Driver ID":driver_id,\
                                "Stops":driver_stops,\
                                    "Pick-UPs":driver_picks,\
                                        "Delivered":driver_delivery,\
                                            "First order Time":first_orders,\
                                                "Last order Time":last_orders})

df_detailed['Date'] = scraped_date
df_detailed['Branch'] = scraped_branch

splitted_stops = df_detailed['Stops'].str.split('/',n=1,expand=True)

df_detailed['Stops Delivered'] = splitted_stops[0]

df_detailed['Stops Target'] = splitted_stops[1]

df_detailed.drop(columns=['Stops'], inplace = True )


splitted_stops = df_detailed['Pick-UPs'].str.split('/',n=1,expand=True)

df_detailed['Picked-UP'] = splitted_stops[0]

df_detailed['Pick-UPs Target'] = splitted_stops[1]

df_detailed.drop(columns=['Pick-UPs'], inplace = True )

splitted_stops = df_detailed['Delivered'].str.split('/',n=1,expand=True)

df_detailed['Delivered Orders'] = splitted_stops[0]

df_detailed['Delivered Target'] = splitted_stops[1]

df_detailed.drop(columns=['Delivered'], inplace = True )
df_detailed.drop_duplicates(subset=['Driver Name',"Driver ID"],inplace=True)
df_detailed.to_excel(f"Detailed Output ({day}-{mon}-{year} for {scraped_branch}.xlsx",index=False)


