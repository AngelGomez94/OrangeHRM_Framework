from pages.login_exitoso import LoginPage

def test_login_exitoso(login_setup):
    driver = login_setup
    login = LoginPage(driver)
    login_exitoso = login.validar_login_exitoso()
    print(login_exitoso)
    assert login_exitoso == "Dashboard", f"Se esperaba el texto 'Dashboard' pero se muestra: {login_exitoso}"
    




