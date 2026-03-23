import pytest
from pages.login_exitoso import LoginPage
from pages.pim_search_page import PinSearchPage
from data.data import USUARIOS, EMPLOYEE_DATA
import time

@pytest.mark.parametrize("user, password", USUARIOS)
def test_pim_busqueda_usuario(driver,user,password):
    login = LoginPage(driver)
    pim = PinSearchPage(driver)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales(user,password)
    pim.abrir_menu_pim()
    pim.buscar_empleado_nombre(EMPLOYEE_DATA['alta_empleado'])
    busqueda_usuario_name = pim.obtener_nombre_usuario()
    assert busqueda_usuario_name == EMPLOYEE_DATA['alta_empleado']['first_name'] + " " + EMPLOYEE_DATA['alta_empleado']['middle_name'] + " " + EMPLOYEE_DATA['alta_empleado']['last_name'], f"El nombre del usuario encontrado '{busqueda_usuario_name}' no coincide con el esperado '{EMPLOYEE_DATA['alta_empleado']['first_name']} {EMPLOYEE_DATA['alta_empleado']['middle_name']} {EMPLOYEE_DATA['alta_empleado']['last_name']}'"
    pim.ir_consultar_usuario()
