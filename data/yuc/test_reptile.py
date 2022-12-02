from unittest import TestCase


import reptile


class Test(TestCase):
    def test_get_doc(self):
        print(reptile.getDoc("https://yuc.wiki/202301"))


class Test2(TestCase):
    url = "https://yuc.wiki/202301"
    def test_parse(self):
        con = reptile.getDoc(Test2.url)
        reptile.parse(con)
