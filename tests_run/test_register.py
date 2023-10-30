import time

import pytest

from DOMs.registerpage import RegisterPage

@pytest.mark.parametrize("name,lastname,email,passwrd,newsletter,chckbx",[("riktor","wiernia","wiertnia@wp.pl","pasrw",True,True ),
                                                                          ("ola","wiernia","wiertnia.ola@wp.pl","pasrw",True,False ),
                                                                          pytest.param("dd","ff","widupa.dslawp.pl","pasrw",True,False, marks=pytest.mark.xfail )])

def testRegister(page, name,lastname,email,passwrd,newsletter,chckbx) -> None:
    registerPage = RegisterPage(page)
    #otwarcie strony do testu
    registerPage.register_run()
    #Wypelnienie formularza
    #test1 dane poprawne
    registerPage.fillOut_form(name, lastname, email,passwrd,newsletter,chckbx)


