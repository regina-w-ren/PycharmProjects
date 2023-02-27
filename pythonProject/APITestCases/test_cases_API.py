from time import sleep

import pytest


class TestLogin():
    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_login1(self):
        print("firstlogin")

    @pytest.mark.run(order=1)
    @pytest.mark.aa
    @pytest.mark.smoke
    def test_login2(self):
        print("secondlogin")
        assert  1==1


    @pytest.mark.run(order=2)
    @pytest.mark.smoke
    def test_login3(self):
        print("thirdlogin")
