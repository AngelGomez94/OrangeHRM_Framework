from selenium.webdriver.chrome.webdriver import WebDriver
from pages.orange_base import BaseOrange
from selenium.webdriver.common.by import By
import allure



class LoginPage(BaseOrange):
 txt_usuario = (By.NAME,"username")
 txt_password = (By.NAME,"password")
 btn_login = (By.XPATH,"//button[contains(.,'Login')]")
 titulo_menu = (By.XPATH,"//h6[contains(.,'Dashboard')]")
 
 def __init__(self, driver: WebDriver):
        super().__init__(driver)

 
 @allure.step("Ingresar credenciales de usuario: {usuario}")

 def ingresar_credenciales(self,usuario,password):
     self.escribir_clickable(self.txt_usuario,usuario)
     self.escribir_clickable(self.txt_password,password)
     self.esperar_y_hacer_click(self.btn_login)
 def validar_login_exitoso(self):
     return self.obtener_texto(self.titulo_menu)
 
 
     