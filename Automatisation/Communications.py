__author__ = 'StefanFlorescu'

from Automatisation.BasePage import BasePage

class Communications(BasePage):

    def access_comunication(self, com):
        self.goto_menuoption(partial_text= com)
