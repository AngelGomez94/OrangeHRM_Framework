import pytest
from pages.login_exitoso import LoginPage
from pages.pim_page import PinPage
from data.data import USUARIOS


@pytest.mark.parametrize("user, password", USUARIOS)
def test_pim(driver,user,password):
    login = LoginPage(driver)
    pim = PinPage(driver)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales(user,password)
    employee_id = pim.generar_idemployee()
    pim.alta_empleado_sin_login("Andres","Gomez","Morales",employee_id)
    toast__alta = pim.validacion_toast_alta_usuario()
    assert toast__alta == "Successfully Saved", f"Se esperaba el texto en el toast Success pero se muestra: {toast__alta}"
    pim.personal_details("Angel123","180000241787","2025-12-31")
    toast_personal_details = pim.validacion_toast_personal_details()
    assert toast_personal_details == "Successfully Updated", f"Se esperaba el texto en el toast Success pero se muestra: {toast_personal_details}"
    pim.custom_fields()
    toast_custom_fields = pim.validacion_toast_custom_fields()
    assert toast_custom_fields == "Successfully Saved", f"Se esperaba el texto en el toast Success pero se muestra: {toast_custom_fields}"
