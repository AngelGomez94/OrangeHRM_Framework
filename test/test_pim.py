import pytest
from pages.login_exitoso import LoginPage
from pages.pim_page import PinPage
from data.data import USUARIOS, EMPLOYEE_DATA


@pytest.mark.parametrize("user, password", USUARIOS)
def test_pim(driver,user,password):
    login = LoginPage(driver)
    pim = PinPage(driver)
    login.abrir_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.ingresar_credenciales(user,password)
    employee_id = pim.abrir_menu_pim()
    pim.alta_empleado_sin_login(EMPLOYEE_DATA['alta_empleado'], employee_id)
    toast__alta = pim.validacion_toast_alta_usuario()
    assert toast__alta == "Successfully Saved", f"Se esperaba el texto en el toast Successfully Updated pero se muestra: {toast__alta}"
    pim.personal_details(EMPLOYEE_DATA['personal_details'])
    toast_personal_details = pim.validacion_toast_personal_details()
    assert toast_personal_details == "Successfully Updated", f"Se esperaba el texto en el toast Success pero se muestra: {toast_personal_details}"
    pim.custom_fields(EMPLOYEE_DATA['custom_fields'])
    toast_custom_fields = pim.validacion_toast_custom_fields()
    assert toast_custom_fields == "Successfully Saved", f"Se esperaba el texto en el toast Success pero se muestra: {toast_custom_fields}"
    pim.contact_details(EMPLOYEE_DATA['contact_details'])
    pim.fill_contact_telephone(EMPLOYEE_DATA['telephone_details'])
    pim.fill_contact_email()
    toast_contact_details = pim.toast_and_wait(pim.toast_suscces)
    assert toast_contact_details == "Successfully Updated", f"Se esperaba el texto en el toast Successfully Updated pero se muestra: {toast_contact_details}"
    pim.emergency_contacts(EMPLOYEE_DATA['emergency_contact'])
    toast_emergency_contact = pim.validacion_toast_emergency_contact()
    assert toast_emergency_contact == "Successfully Saved", f"Se esperaba el texto en el toast Successfully Saved pero se muestra: {toast_emergency_contact}"
    pim.assigned_dependents(EMPLOYEE_DATA['dependents'])
    toast_dependents = pim.validacion_toast_dependents()
    assert toast_dependents == "Successfully Saved", f"Se esperaba el texto en el toast Successfully Saved pero se muestra: {toast_dependents}"
    pim.fill_inmigration(EMPLOYEE_DATA['inmigration'])
    