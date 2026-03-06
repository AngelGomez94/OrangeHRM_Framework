from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import uuid
from selenium.webdriver.common.by import By
class BaseOrange:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def abrir_url(self, url):
        self.driver.get(url) ##El navegador se definio en el conftest.py

    def esperar_y_hacer_click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Metodo para escribir en un campo de texto, primero espera a que el elemento sea clickable, luego hace click y escribe el texto    
    def escribir_clickable(self, locator, texto):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            elemento.click()
        except Exception:
            pass # Si el click falla, se ignora el error y se continúa con la escritura
        elemento.clear()
        elemento.send_keys(texto)

    def subir_foto(self,locator,ruta):
        foto = self.wait.until(EC.presence_of_element_located(locator))
        foto.send_keys(ruta)

    def borrar_y_escribir(self,locator,texto): #Eliminar el texto por default de un txt
        elemento = self.wait.until(EC.visibility_of_element_located(locator))
        elemento.send_keys(Keys.CONTROL + "a")
        elemento.send_keys(Keys.BACKSPACE)
        elemento.send_keys(texto)
    def obtener_texto(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    def obtener_menu_actual(self):
         return self.driver.current_url
    def indicar_menu_actual(self,locador):
        return self.wait.until(EC.visibility_of_element_located(locador)).text
    def generar_idemployee(self):
        return uuid.uuid4().hex[:8]
    def toast(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def toast_and_wait(self, locator):
        """Return toast text and wait until it disappears.

        This helps prevent capturing the same toast multiple times when
        toasts appear quickly one after another.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        self.wait.until(EC.invisibility_of_element_located(locator))
        return text
    def esperar_url_contenga(self,sub_url):
        self.wait.until(EC.url_contains(sub_url))
    def esperar_elemento_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    def esperar_spinner_desaparecer(self,locator):
        self.wait.until(EC.invisibility_of_element_located(locator))
    def llenar_datepicker(self,locator,fecha):

        #date_string = datetime.date.today().strftime("%Y-%m-%d")
        date_input = self.wait.until(EC.element_to_be_clickable(locator))
        date_input.click()
        date_input.clear()
        date_input.send_keys(fecha)
        date_input.click()
    def llenar_dropdown(self,locator,opcion):
        dropdown = self.wait.until(EC.element_to_be_clickable(locator))
        dropdown.click()
        
        # XPath que busca el span de texto dentro del div con role='option'
        opcion_locator = (By.XPATH, f"//div[@role='option']//span[contains(text(), '{opcion}')]")
        
        try:
            option_element = self.wait.until(EC.element_to_be_clickable(opcion_locator))
            option_element.click()
        except Exception as e:
            # Si falla, intentar con JavaScript
            option_element = self.driver.find_element(*opcion_locator)
            self.driver.execute_script("arguments[0].click();", option_element)


       

 
        