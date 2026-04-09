from selenium.webdriver.chrome.webdriver import WebDriver
from pages.orange_base import BaseOrange
from selenium.webdriver.common.by import By
import time

class PinSearchPage(BaseOrange):
  
  txt_usuario = (By.NAME,"username")
  txt_password = (By.NAME,"password")
  btn_login = (By.XPATH,"//button[contains(.,'Login')]")
  menu_pim = (By.XPATH, "//span[text()='PIM']")
  txt_employe_name = (By.XPATH,"(//input[@placeholder='Type for hints...'])[1]")
  btn_search_user = (By.XPATH,"//button[contains(.,'Search')]")
  record_user = (By.XPATH,"(//div[contains(text(),'Pruebita QAtito')])[1]")
  results_record = (By.XPATH,"//div[@role='option']//span[contains(text(), 'Pruebita QAtito Petro')]")
  cell_name = (By.XPATH,"//div[@class='oxd-table-card']//div[@role='cell'][3]")
  cell_lastname = (By.XPATH,"//div[@class='oxd-table-card']//div[@role='cell'][4]")




  
  def __init__(self, driver: WebDriver):
        super().__init__(driver)
  
  
  def ingresar_credenciales(self,usuario,password):
     self.escribir_clickable(self.txt_usuario,usuario)
     self.escribir_clickable(self.txt_password,password)
     self.esperar_y_hacer_click(self.btn_login)
  
  def buscar_empleado_nombre(self,data):
      self.esperar_y_hacer_click(self.menu_pim)
      self.escribir_clickable(self.txt_employe_name,data['first_name'] + " " + data['middle_name'] + " " + data['last_name'])
      self.esperar_texto_en_elemento(self.results_record,data['first_name'] + " " + data['middle_name'] + " " + data['last_name']) 
      self.esperar_y_hacer_click(self.results_record)
      self.esperar_y_hacer_click(self.btn_search_user)
  def obtener_nombre_usuario(self):
      return self.obtener_nombre_tabla_busqueda(self.cell_name,self.cell_lastname)
  def ir_consultar_usuario(self):
      self.esperar_y_hacer_click(self.record_user)
      


      
