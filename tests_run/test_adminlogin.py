import pytest

from adminDOMs.adminpage import AdminPage
from utils.secret_config import PASSWORD, USERNAME


@pytest.mark.parametrize("username, passw", [(USERNAME, PASSWORD),
                                        pytest.param('fakeemail', 'fakepassword', marks=pytest.mark.xfail)])
def test_loginadmin(page, username, passw) -> None:
    adminpage = AdminPage(page)  # Zakładając, że zmienna 'page' jest zdefiniowana wcześniej
    adminpage.admin_run()
    adminpage.fillOutForm(username, passw)
