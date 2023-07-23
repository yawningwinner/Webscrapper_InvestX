import selenium
import pandas as pd
import csv
import xlsxwriter
from xlsxwriter import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()
        # self.implicitly_wait(15)
        
    def land_first_page(self):
        self.get("https://sso.definedge.com/auth/realms/definedge/protocol/openid-connect/auth?response_type=code&client_id=opstra&redirect_uri=https://opstra.definedge.com/ssologin&state=e2cf559f-356c-425a-87e3-032097f643d0&login=true&scope=openid")
        # super(Booking, self).__init__()
        # self.implicitly_wait(15)
        self.maximize_window()
    def login(self,email,password):
        self.implicitly_wait(15)
        username = self.find_element(By.ID, 'username')
        username.send_keys(email)
        passw = self.find_element(By.ID, 'password')
        passw.send_keys(password)
        login = self.find_element(By.ID , 'kc-login')
        login.click()
    def kaamka_page(self):
        pehle = self.find_element(By.LINK_TEXT, 'BUILDER')
        pehle.click()
    def open_data(self):
        self.implicitly_wait(7)
        ispe_click = self.find_element(By.CLASS_NAME, 'v-expansion-panel__header__icon')
        ispe_click.click()
        # next_date = self.find_element(By.XPATH, '/html/body/div/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[1]/div[2]/button/div')
        # print(next_date.text)
        # next_date.click()
    def lets_date(self,index):
        xpath_id = f'/html/body/div/div[62]/main/div/div/div/div/div[3]/div[2]/div[3]/ul/li/div[2]/div[1]/div[{index}]/button/div'
        next_date = self.find_element(By.XPATH, xpath_id)
        next_date.click()
        return next_date.text
    def column_name(self):
        data_Table = self.find_element(By.CLASS_NAME, 'v-table__overflow')
        col_ka_data = []
        topper = data_Table.find_element(By.TAG_NAME, 'thead')
        heads = topper.find_elements(By.TAG_NAME, 'th')
        for head in heads:
            row_ka_data = [head.text]
            col_ka_data.append(row_ka_data)
        print(col_ka_data)
        return col_ka_data
    def data_extract(self,date=None):
        print("data extraction shuruu")
        data_Table = self.find_element(By.CLASS_NAME, 'v-table__overflow')
        extracted_Data = []
        body = data_Table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')
        for row in rows :
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_ka_data = [cell.text for cell in cells]
            extracted_Data.append(row_ka_data)
        print("khatam")
        return extracted_Data
    def create_csvfile(self,date,scraped_data,col_ka_data):
        column_names = [col[0] for col in col_ka_data]
        df = pd.DataFrame(scraped_data, columns=column_names)
        name= f'scraped_table_data_{date}.xlsx'
        excel_writer = pd.ExcelWriter(name, engine='xlsxwriter')
        sheet_name = f'Sheet_{date}'
        df.to_excel(excel_writer, sheet_name=sheet_name, index=False)
        excel_writer.close()
        print(f"Data of {date} chala gya to" + name)

    # def __exit__(self, exc_type, exc_value, trace):
    #     if self.teardown:
    #         self.quit()


