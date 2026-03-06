import pytest
from pages.login_exitoso import LoginPage
from data.data import USUARIOS

@pytest.mark.parametrize("user, password", USUARIOS)
def test_login_exitoso(driver,user,password):
    login = LoginPage(driver)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    menu_actual = login.ingresar_credenciales(user,password)
    assert menu_actual == "Dashboard", f"No se mostro el dashboard despues de hacer login"
 




