from pages.pim_search_page import PinSearchPage
from data.data import USUARIOS, EMPLOYEE_DATA
import time


def test_pim_busqueda_usuario(login_setup):
    driver = login_setup
    pim = PinSearchPage(driver)
    pim.abrir_menu_pim()
    pim.buscar_empleado_nombre(EMPLOYEE_DATA['alta_empleado'])
    busqueda_usuario_name = pim.obtener_nombre_usuario()
    assert busqueda_usuario_name == EMPLOYEE_DATA['alta_empleado']['first_name'] + " " + EMPLOYEE_DATA['alta_empleado']['middle_name'] + " " + EMPLOYEE_DATA['alta_empleado']['last_name'], f"El nombre del usuario encontrado '{busqueda_usuario_name}' no coincide con el esperado '{EMPLOYEE_DATA['alta_empleado']['first_name']} {EMPLOYEE_DATA['alta_empleado']['middle_name']} {EMPLOYEE_DATA['alta_empleado']['last_name']}'"
    pim.ir_consultar_usuario()
