import pytest

from adminDOMs.adminpage import AdminPage
from utils.secret_config import PASSWORD, USERNAME


@pytest.mark.parametrize("username, passw", [(USERNAME, PASSWORD)])
def test_mainpanel(page, username, passw) -> None:
    adminpage = AdminPage(page)
    adminpage.admin_run()
    adminpage.fillOutForm(username, passw)
    adminpage.mainpanel()