__author__ = 'StefanFlorescu'

from Automatisation.BasePage import BasePage

class Communications(BasePage):

    def access_comunication(self, communication_cathegory):
        self.goto_menuoption(partial_text= communication_cathegory)
