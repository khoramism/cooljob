from playwright.sync_api import sync_playwright

site = 'https://careers.tapsi.ir/jobs'

def get_job_details(browser, job_url):
    context = browser.new_context()
    page = context.new_page()
    page.goto(job_url)
    page.wait_for_selector('div._1FW-s')

    detail_text = page.query_selector_all('div._1FW-s')[0].inner_text().strip()

    context.close()
    return detail_text

def run_tapsi(playwright):
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
        job_data = {
            'title': position,
            'team': team,
            'location': city,
            'url': full_url,
            'detail' : detail,
            'company': 'tapsi'
        }
        jobs_data.append(job_data)
    browser.close()
    return jobs_data

