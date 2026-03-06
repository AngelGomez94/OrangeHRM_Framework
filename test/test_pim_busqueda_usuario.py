import pytest
from pages.login_exitoso import LoginPage
from pages.pim_page import PinPage
from data.data import USUARIOS

@pytest.mark.parametrize("user, password", USUARIOS)
def test_pim_busqueda_usuario(driver,user,password):
    login = LoginPage(driver)
    pim = PinPage(driver)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales(user,password)
    pim.abrir_menu_pim()
    