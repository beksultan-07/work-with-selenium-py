# import openpyxl
# def pars_excel():
    # wb = openpyxl.reader.excel.load_workbook(filename = 'Авито+сбор+разовый+(1).xlsx')
    # wb.active = 0
    # sheet = wb.active
    # # print(sheet['A1'].value)
    # urls = []
    # def get_urls(maxN, minN):
    #     urlsF = []
    #     for i in range(maxN,minN):
    #         urlsF.append(sheet['B'+str(i)].value)
    #     return urlsF
    # urls += get_urls(6, 21)
    # urls += get_urls(22, 37)
    # urls += get_urls(38, 52)
    # return urls


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from library import get_info


info = []

def get_urls_from_page(URL):
    try:
        driver = webdriver.Chrome()
        driver.get(URL)
        time.sleep(30)
        href = 'https://www.avito.ru'
        height = driver.execute_script("return document.body.scrollHeight")

        print(height)
        links = []
        for item in range (0, height, 50):
            driver.execute_script(f"window.scrollTo(0, {item})")

            links = driver.find_elements_by_css_selector('.link-link-39EVK.link-design-default-2sPEv.title-root-395AQ.iva-item-title-1Rmmj.title-listRedesign-3RaU2.title-root_maxHeight-3obWc')

        index = 0
        for i in links:
            i.click()
            index += 1
            info.append(get_info(driver, index))

    finally:
        driver.quit()

get_urls_from_page("https://www.avito.ru/moskva_i_mo/predlozheniya_uslug/transport_perevozki/spetstekhnika-ASgBAgICAkSYC8SfAZoL3J8B?cd=1")