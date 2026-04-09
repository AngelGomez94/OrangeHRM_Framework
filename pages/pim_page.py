from selenium.webdriver.chrome.webdriver import WebDriver
from pages.orange_base import BaseOrange
from selenium.webdriver.common.by import By
import os
from faker import Faker
import allure

class PinPage(BaseOrange):
 # generador Faker de uso compartido
 faker = Faker()
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
 expitarion_date = (By.XPATH,"//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//input")
 emergency_contact = (By.XPATH,"//label[text()='Emergency Contact']/parent::div/following-sibling::div/input")
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
 home_phone = (By.XPATH,"//label[text()='Home']/parent::div/following-sibling::div/input")
 mobile_phone = (By.XPATH, "//label[text()='Mobile']/parent::div/following-sibling::div/input")
 work_phone = (By.XPATH, "//label[text() = 'Work']/parent::div/following-sibling::div/input ")
 work_email = (By.XPATH,"//label[text() = 'Work Email']/parent::div/following-sibling::div/input")
 other_email = (By.XPATH,"//label[text()='Other Email']/parent::div/following-sibling::div/input")
 emergency_contact_menu = (By.XPATH,"//a[normalize-space()='Emergency Contacts']")
 add_emergency_contact = (By.XPATH,"//h6[contains(.,'Assigned Emergency Contacts')]/following::button[1]")
 contact_emergency_name = (By.XPATH,"//label[text()='Name']/parent::div/following-sibling::div/input")
 contact_relationship = (By.XPATH,"//label[text()='Relationship']/parent::div/following-sibling::div/input")
 contact_home_phone = (By.XPATH,"//label[text()='Home Telephone']/parent::div/following-sibling::div/input")
 contact_mobile_phone = (By.XPATH,"//label[text()='Mobile']/parent::div/following-sibling::div/input")
 contact_work_phone = (By.XPATH,"//label[text()='Work Telephone']/parent::div/following-sibling::div/input")
 btn_save_emergency_contact = (By.XPATH,"(//button[normalize-space()='Save'])[1]")
 dependets_menu = (By.XPATH,"//a[normalize-space()='Dependents']")
 add_dependent = (By.XPATH,"//h6[contains(.,'Assigned Dependents')]/following::button[1]")
 dependent_name = (By.XPATH,"//label[text() = 'Name']/parent::div/following-sibling::div/input")
 dependent_relationship = (By.XPATH,"//label[text()='Relationship']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 specific_dependent = (By.XPATH,"//label[text()='Please Specify']/parent::div/following-sibling::div/input")
 dependent_date_birth = (By.XPATH, "//label[text()='Date of Birth']/parent::div/following-sibling::div//input")
 btn_save_dependent =(By.XPATH,"(//button[normalize-space()='Save'])[1]")
 inmigration_menu =(By.XPATH,"//a[normalize-space()='Immigration']")
 add_inmigration = (By.XPATH,"//h6[contains(.,'Assigned Immigration Records')]/following::button[1]")
 passport = (By.XPATH,"//label[text()='Passport']")
 visa = (By.XPATH,"//label[text()='Visa']")
 number_document = (By.XPATH,"//label[text()='Number']/parent::div/following-sibling::div//input")
 document_issued_date =(By.XPATH,"//label[text()='Issued Date']/parent::div/following-sibling::div//input")
 document_expiration_date = (By.XPATH,"//label[text()='Expiry Date']/parent::div/following-sibling::div//input")
 document_status = (By.XPATH,"//label[text()='Eligible Status']/parent::div/following-sibling::div/input")
 document_issued_by = (By.XPATH,"//label[text()='Issued By']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 document_review_date = (By.XPATH,"//label[text()='Eligible Review Date']/parent::div/following-sibling::div//input")
 document_comments = (By.XPATH,"//label[text()='Comments']/parent::div/following-sibling::div//textarea")
 btn_save_inmigration =(By.XPATH,"(//button[normalize-space()='Save'])[1]")
 job_joined_date = (By.XPATH,"//label[text()= 'Joined Date']/parent::div/following-sibling::div//input")
 job_title = (By.XPATH,"//label[text()='Job Title']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 job_category = (By.XPATH, "//label[text()='Job Category']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 job_sub_unit = (By.XPATH,"//label[text()='Sub Unit']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 job_location = (By.XPATH,"//label[text()='Location']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 employment_status = (By.XPATH, "//label[text()='Employment Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
 contract_details_input = (By.XPATH,"//input[@type='checkbox']")
 contract_details_switch = (By.XPATH,"//span[contains(@class, 'oxd-switch-input')]")
 contract_start_date = (By.XPATH, "//label[text()= 'Joined Date']/parent::div/following-sibling::div//input")
 contract_end_date = (By.XPATH,"//label[text()= 'Contract End Date']/parent::div/following-sibling::div//input")


 def __init__(self, driver: WebDriver):
        super().__init__(driver)

 
 @allure.step("Alta de empleado sin login con datos: {data} y ID: {employe_id}")
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
 @allure.step("Validación toast de alta de empleado")    
 def validacion_toast_alta_usuario(self):
      return self.toast_and_wait(self.toast_suscces)
 
 @allure.step("Llenar detalles personales")
 def personal_details(self, data):
    # Esperar a que el spinner desaparezca y asegurarse de que los campos sean interactuables
    self.esperar_spinner_desaparecer(self.spiner)
    self.escribir_clickable(self.txt_other_id, data['other_id'])
    self.escribir_clickable(self.txt_license_number, data['license_number'])
    self.llenar_datepicker(self.txt_license_exp, data['license_exp'])
    self.llenar_dropdown(self.txt_nationality, data['nationality'])
    self.llenar_dropdown(self.txt_marital_status, data['marital_status'])
    self.llenar_datepicker(self.txt_date_birth, data['date_of_birth'])
    self.llenar_radio_button(self.male, self.female)
    self.esperar_y_hacer_click(self.btn_personal_details)
    
 @allure.step("Validación toast de detalles personales")
 def validacion_toast_personal_details(self):
      return self.toast_and_wait(self.toast_suscces)
 
 
 @allure.step("Llenar campos personalizados")
 def custom_fields(self,data):
     self.llenar_dropdown(self.blod_type,data['blood_type'])
     self.esperar_y_hacer_click(self.btn_save_custom_fields)
 @allure.step("Validación toast de campos personalizados")
 def validacion_toast_custom_fields(self):
         return self.toast_and_wait(self.toast_suscces)
 @allure.step("Llenar detalles de contacto")
 def contact_details(self,data):
     self.esperar_y_hacer_click(self.contact_details_menu)
     self.esperar_spinner_desaparecer(self.spiner)
     self.escribir_clickable(self.txt_street1,data['street1'])
     self.escribir_clickable(self.txt_street2,data['street2'])
     self.escribir_clickable(self.txt_city,data['city'])
     self.escribir_clickable(self.txt_state,data['state'])
     self.escribir_clickable(self.txt_postal_code,data['zip_code'])
     self.llenar_dropdown(self.dropdown_country,data['country'])
 
 @allure.step("Llenar detalles de contacto (telefonos)")
 def fill_contact_telephone(self,data):
     self.escribir_clickable(self.home_phone,data['home_phone'])
     self.escribir_clickable(self.mobile_phone,data['mobile'])
     self.escribir_clickable(self.work_phone,data['work_phone'])
 
 @allure.step("Llenar detalles de contacto (emails)")
 def fill_contact_email(self):
     unique_email = self.faker.email()
     other_email = self.faker.email()
     self.escribir_clickable(self.work_email, unique_email)
     self.escribir_clickable(self.other_email, other_email)
     self.esperar_y_hacer_click(self.btn_personal_details)

 
 @allure.step("Validación toast de detalles de contacto")
 def contact_details_toast(self):
     return self.toast_and_wait(self.toast_suscces)

 @allure.step("Validación toast de campos personalizados")
 def custom_fields_contact_details_toast(self):
     return self.toast_and_wait(self.toast_suscces)
 
 @allure.step("Llenar contactos de emergencia")
 def emergency_contacts(self,data):
        self.esperar_y_hacer_click(self.emergency_contact_menu)
        self.esperar_y_hacer_click(self.add_emergency_contact)
        self.escribir_clickable(self.contact_emergency_name,data['name'])
        self.escribir_clickable(self.contact_relationship,data['relationship'])
        self.escribir_clickable(self.contact_home_phone,data['home_phone'])
        self.escribir_clickable(self.contact_mobile_phone,data['mobile'])
        self.escribir_clickable(self.contact_work_phone,data['work_phone'])
        self.esperar_y_hacer_click(self.btn_save_emergency_contact)

 @allure.step("Validación toast de contactos de emergencia")
 def validacion_toast_emergency_contact(self):
        return self.toast_and_wait(self.toast_suscces)
 
 @allure.step("Llenar dependientes")
 def assigned_dependents(self,data):
      self.esperar_y_hacer_click(self.dependets_menu)
      self.esperar_y_hacer_click(self.add_dependent)
      self.escribir_clickable(self.dependent_name,data['name'])
      self.llenar_dropdown(self.dependent_relationship,data['relationship'])
      self.escribir_clickable(self.specific_dependent,data['specific_relationship'])
      self.llenar_datepicker(self.dependent_date_birth,data['date_of_birth'])
      self.esperar_y_hacer_click(self.btn_save_dependent)
 
 @allure.step("Validación toast de dependientes")
 def validacion_toast_dependents(self):
      return self.toast_and_wait(self.toast_suscces)
 
 @allure.step("Llenar información de inmigración")
 def fill_inmigration(self,data):
      self.esperar_y_hacer_click(self.inmigration_menu)
      self.esperar_y_hacer_click(self.add_inmigration)
      self.llenar_radio_button(self.passport,self.visa)
      self.escribir_clickable(self.number_document,data['number_document'])
      self.llenar_datepicker(self.document_issued_date,data['document_issued_date'])
      self.llenar_datepicker(self.document_expiration_date,data['document_expiration_date'])
      self.escribir_clickable(self.document_status,data['document_status'])
      self.llenar_dropdown(self.document_issued_by,data['document_issued_by'])
      self.llenar_datepicker(self.document_review_date,data['document_review_date'])
      self.escribir_clickable(self.document_comments,data['document_comments'])
      self.esperar_y_hacer_click(self.btn_save_inmigration)
 
 @allure.step("Validación toast de información de inmigración")
 def validacion_toast_inmigration(self):
      return self.toast_and_wait(self.toast_suscces)
 

      
     

 
 

  
    
     
