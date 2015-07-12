__author__ = 'StefanFlorescu'

from  Automatisation.pages import LoginPage
import unittest

class LOG (unittest.TestCase):

    def test_LoginProcedure(self):
        LoginPage.GoTo()
        LoginPage.AgLogin()

if __name__ == '__main__':
    unittest.main()

