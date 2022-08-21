from selenium import webdriver
class Connection:
     def __init__(self,path,headless=False):
         from selenium.webdriver.chrome.options import Options
         option = Options()
         option.add_argument('--disable-extensions')
         if(headless):
            option.add_argument('--headless')
         self.driver = webdriver.Chrome(executable_path=path,options=option)
     def load(self,url):
         return self.driver.get(url)
    #  def cari_name(self,name):
    #  def cari_id(self,id):
    #  def cari_class(self,kelas):
    #  def clear(self):
    #  def quit(self):