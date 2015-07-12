__author__ = 'Steve'

from selenium import webdriver

class Browser (object):

    def __init__(self):
        self._webdriver = webdriver.Firefox()
        self._url = 'https://letrisks-acumen.com'

    def go(self):
        """
        :rtype : object
        """
        self._webdriver.get(self._url)

    def close(self):
        self._webdriver.close()

    @property
    def title(self):
        return self._webdriver.title

    @property
    def webdriver(self):
        return self._webdriver


if __name__ == '__main__':
    x = Browser()
    x.GoTo()
    print x.title
    x.Close()