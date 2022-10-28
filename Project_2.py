from bs4 import BeautifulSoup as bs
import requests as r

#requesting website
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
req = r.get(url)

#Extracting HTML code from the website
html_code = req.text

#Using soup to extract info
soup = bs(html_code, 'lxml')
job = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for company_name in job:
    company_nam = company_name.find('h3', class_ = 'joblist-comp-name').text.replace(" ", "")
    print(company_nam)


print("Program ran successully!")
