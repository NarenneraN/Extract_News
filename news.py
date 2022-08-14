from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'
path = 'E:\MY_WORKS\chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

titles=[]
subtitles=[]

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
for container in containers:
    title = container.find_element(by="xpath",value='./a/h2')
    subtitle = container.find_element(by="xpath", value='./a/p')
    titles.append(title.text)
    subtitles.append(subtitle.text)

samples = {'Title : ':titles,'Subtitles: ':subtitles}
df_headlines = pd.DataFrame(samples)
df_headlines.to_csv('headlines1.csv')
driver.quit()