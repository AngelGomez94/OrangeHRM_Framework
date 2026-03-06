from selenium.webdriver.chrome.webdriver import WebDriver
from pages.orange_base import BaseOrange
from selenium.webdriver.common.by import By
import os
import random


class PinPage(BaseOrange):
 menu_pim = (By.XPATH, "//span[text()='PIM']")
 btn_add_employee = (By.XPATH,"//button[contains(.,' Add ')]")
 txt_usuario = (By.NAME,"username")
 txt_password = (By.NAME,"password")
 btn_login = (By.XPATH,"//button[contains(.,'Login')]")
 txt_first_name = (By.NAME ,"firstName")
 txt_middle_name = (By.NAME, "middleName")
 txt_last_name = (By.NAME, "lastName")
 txt_employe_id = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
 btn_foto = (By.XPATH,"//input[@type='file']") 
 btn_save_employee = (By.XPATH, "//button[contains(.,'Save')]")
 toast_suscces = (By.CSS_SELECTOR, ".oxd-toast-content p:last-child")
 txt_other_id = (By.XPATH, "//label[text()='Other Id']/following::input[1]")
 txt_license_number = (By.XPATH, "//label[text()=\"Driver's License Number\"]/parent::div/following-sibling::div/input")
 txt_license_exp = (By.XPATH, "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input")
 txt_marital_status = (By.XPATH, "//label[text()='Marital Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 txt_nationality = (By.XPATH, "//label[text()='Nationality']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 txt_date_birth = (By.XPATH, "//label[text()='Date of Birth']/parent::div/following-sibling::div//input")
 male = (By.XPATH, "//label[text()='Male']")
 female = (By.XPATH,"//label[text()='Female']")
 spiner = (By.CLASS_NAME,"oxd-loading-spinner")
 txt_nationality = (By.XPATH, "//label[text()='Nationality']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 expitarion_date = (By.XPATH,"//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input")
 txt_marital_status = (By.XPATH,"//label[text()='Marital Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 txt_date_birth =(By.XPATH,"//label[text()='Date of Birth']/parent::div/following-sibling::div//div//input")
 btn_personal_details = (By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]")
 blod_type = (By.XPATH,"//label[text()='Blood Type']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 btn_save_custom_fields = (By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[2]")
 toast_personal_details = (By.CSS_SELECTOR, ".oxd-toast-content p:last-child")
 toast_custom_fields = (By.CSS_SELECTOR, ".oxd-toast-content p:last-child")
 contact_details_menu = (By.XPATH,"//a[normalize-space()='Contact Details']")
 txt_street1 = (By.XPATH,"//label[text()='Street 1']/parent::div/following-sibling::div/input")
 txt_street2 = (By.XPATH,"//label[text()='Street 2']/parent::div/following-sibling::div/input")
 txt_city = (By.XPATH,"//label[text()='City']/parent::div/following-sibling::div/input")
 txt_state = (By.XPATH,"//label[text()='State/Province']/parent::div/following-sibling::div/input")
 txt_postal_code = (By.XPATH,"//label[text()='Zip/Postal Code']/parent::div/following-sibling::div/input")
 dropdown_country = (By.XPATH,"//label[text()='Country']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")


 def __init__(self, driver: WebDriver):
        super().__init__(driver)

 def ingresar_credenciales(self,usuario,password):
     self.escribir_clickable(self.txt_usuario,usuario)
     self.escribir_clickable(self.txt_password,password)
     self.esperar_y_hacer_click(self.btn_login)
 
 def alta_empleado_sin_login(self,data,employe_id):
     self.esperar_y_hacer_click(self.menu_pim)
     self.esperar_y_hacer_click(self.btn_add_employee)
     self.escribir_clickable(self.txt_first_name,data['first_name'])
     self.escribir_clickable(self.txt_middle_name,data['middle_name'])
     self.escribir_clickable(self.txt_last_name,data['last_name'])
     self.borrar_y_escribir(self.txt_employe_id,employe_id)
     ruta_foto = os.path.abspath("./data/foto.jpg")
     self.subir_foto(self.btn_foto,ruta_foto)
     self.esperar_y_hacer_click(self.btn_save_employee)
 def validacion_toast_alta_usuario(self):
      return self.toast_and_wait(self.toast_suscces)
 def personal_details(self, data):
    # Esperar a que el spinner desaparezca y asegurarse de que los campos sean interactuables
    self.esperar_spinner_desaparecer(self.spiner)
    self.escribir_clickable(self.txt_other_id, data['other_id'])
    self.escribir_clickable(self.txt_license_number, data['license_number'])
    self.llenar_datepicker(self.txt_license_exp, data['license_exp'])
    self.llenar_dropdown(self.txt_nationality, data['nationality'])
    self.llenar_dropdown(self.txt_marital_status, data['marital_status'])
    self.llenar_datepicker(self.txt_date_birth, data['date_of_birth'])
    valor_genero = random.choice([True, False])
    if valor_genero:
        self.esperar_y_hacer_click(self.male)
    else:
        self.esperar_y_hacer_click(self.female)
    self.esperar_y_hacer_click(self.btn_personal_details)
 def validacion_toast_personal_details(self):
      return self.toast_and_wait(self.toast_suscces)
 
 def custom_fields(self,data):
     self.llenar_dropdown(self.blod_type, data['blood_type'])
     self.esperar_y_hacer_click(self.btn_save_custom_fields)
 def validacion_toast_custom_fields(self):
         return self.toast_and_wait(self.toast_suscces)
 def contact_details(self,data):
     self.esperar_y_hacer_click(self.contact_details_menu)
     self.escribir_clickable(self.txt_street1,data['street1'])
     self.escribir_clickable(self.txt_street2,data['street2'])
     self.escribir_clickable(self.txt_city,data['city'])
     self.escribir_clickable(self.txt_state,data['state'])
     self.escribir_clickable(self.txt_postal_code,data['zip_code'])
     self.llenar_dropdown(self.dropdown_country,data['country'])
         

  
    
     
