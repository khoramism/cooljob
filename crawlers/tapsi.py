from bs4 import BeautifulSoup
import requests

site = 'https://careers.tapsi.ir/jobs'

# def get_list():
#     resp = requests.get(site)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     # print(resp.text)
#     job_list = []
#     # print(soup.body.div.div.main)
#     print(soup.body.div.div.main.find_all('div', attrs={'class':'_3kFn5'}))

#     for job in soup.find_all('a', attrs= {'class' :'_1sQNY _1z8Oj'}):
#         print(job)
#         title = job.find('p', class_='kIgse').text.strip()
#         department = job.find('div', class_='_13F5M').text.strip()
#         location = job.find('li', class_='_13F5M').text.strip()
#         url = site[:-1] + job.get('href')
#         # job_detail = get_detail(url)

#         job_dict = {
#             'title': title,
#             'department': department,
#             'location': location,
#             'url': url, 
#             # 'job_detail' : job_detail
#         }
#         job_list.append(job_dict)
#     return job_list

# def get_detail(url: str):
#     class_content = 'col-md-9 content'
#     resp = requests.get(url)
#     soup = BeautifulSoup(resp.text, 'html.parser')
#     print(soup.find('div', attrs={'class' : class_content}).text)

# jobs = get_list()
# for job in jobs:
#     print(job)

from playwright.sync_api import sync_playwright

def get_job_details(browser, job_url):
    # Open a new page in a new context for each job detail
    context = browser.new_context()
    page = context.new_page()
    print(job_url)
    page.goto(job_url)
    page.wait_for_selector('div._1FW-s')

    # description_paragraphs = page.query_selector_all('div._1FW-s > div > p')
    # description_list_items = page.query_selector_all('div._1FW-s > div > ul > li')

        # Combine the paragraphs and list items into a single description string
    detail_text = page.query_selector_all('div._1FW-s')[0].inner_text().strip()

    context.close()
    return detail_text

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(site) 
    page.wait_for_selector('a._1sQNY._1z8Oj')
    job_listings = page.query_selector_all('a._1sQNY._1z8Oj')

    jobs_data = []
    for job_element in job_listings:
        position_element = job_element.query_selector('p.kIgse')
        team_element = job_element.query_selector('div:nth-child(2) > p._13F5M')  # Adjusted selector
        city_element = job_element.query_selector('div:nth-child(3) > p._13F5M')  # Adjusted selector

        position = position_element.inner_text().strip() if position_element else "N/A"
        team = team_element.inner_text().strip() if team_element else "N/A"
        city = city_element.inner_text().strip() if city_element else "N/A"
        url = job_element.get_attribute('href').split('/')[-1]
        full_url = page.url + "/" + url if url else "N/A"
        
        detail = get_job_details(browser=browser, job_url=full_url)
        print(detail)
        job_data = {
            'position': position,
            'team': team,
            'city': city,
            'url': full_url,
            'detail' : detail
        }
        jobs_data.append(job_data)

    # Close the browser
    browser.close()
    return jobs_data

# Run the Playwright script and print the job details
with sync_playwright() as playwright:
    job_details = run(playwright)
    for job in job_details:
        print(job)
