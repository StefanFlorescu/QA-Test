__author__ = 'StefanFlorescu'

mass = [
    {"name": ['RAYMOND ', 'SMITH ', '01/11/1945'], "address": ['3 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['ROGER ', 'HAYNE ', '01/11/1951'], "address": ['5 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['BEN ', 'SKUTANS ', '01/01/1976'], "address": ['6 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Co-habiting"], "ccj": False, "phone": False},
    {"name": ['John ', 'SKUTANS ', '01/06/1937'], "address": ['8 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Co-habiting"], "ccj": False, "phone": True},
    {"name": ['AMANDA ', 'RIDLINGTON', '01/11/1969'], "address": ['15 ', '16 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Ms", "Female", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['ELIZABETH ', 'STOREY ', '01/04/1961'], "address": ['19 ', '22 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Ms", "Female", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['KEVIN ', 'FRYER', '01/10/1963'], "address": ['20 ', '19 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['ROBERT', 'TAMDY', '01/06/1965'], "address": ['25 ', '26 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['RUTH ', 'GOODWIN', '01/12/1976'], "address": ['385 ', '386 ', '387 '], "bank": ['56-00-36', '44444443'],
     "details": ["Mr", "Male", "British", "Single"], "ccj": False, "phone": True},
    {"name": ['BRIAN ', 'CLARKSON ', '01/03/1940'], "address": ['313 ', '310 ', '316 '],
     "bank": ['56-00-36', '22222221'], "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['BRIAN ', 'KERSHAW', '01/11/1968'], "address": ['518 ', '', ''], "bank": ['56-00-36', '22222221'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['JEFFREY ', 'LAWRENCE ', '01/11/1950'], "address": ['41 ', '39 ', ''], "bank": ['30-91-97', '77777771'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['JEFFREY ', 'WOODCOCK', '01/09/1961'], "address": ['404 ', '', ''], "bank": ['30-91-97', '77777771'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['KARL ', 'TOWNEND', '01/12/1971'], "address": ['474 ', '473 ', ''], "bank": ['07-01-16', '11111118'],
     "details": ["Mr", "Male", "British", "Civil Partnership"], "ccj": True, "phone": False},
    {"name": ['DAVID ', 'COLE', '01/08/1963'], "address": ['127 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Co-habiting"], "ccj": False, "phone": False},
    {"name": ['DAVID ', 'PHILIPS', '01/07/1962'], "address": ['240 ', '239 ', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Single"], "ccj": False, "phone": False},
    {"name": ['DAVID ', 'WISHART', '01/07/1956'], "address": ['245 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['DAVID ', 'SOUTHERN', '01/02/1970'], "address": ['417 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": False, "phone": True},
    {"name": ['DAVID ', 'TURNER', '01/12/1957'], "address": ['442 ', '444 ', '443 '], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Separated"], "ccj": False, "phone": False},
    {"name": ['CERI ', 'TOULMAN', '01/12/1957'], "address": ['444 ', '445 ', '442 '], "bank": ['56-00-36', '40308669'],
     "details": ["Miss", "Female", "British", "Single"], "ccj": False, "phone": False},
    {"name": ['CHRIS ', 'JACKSON', '01/05/1948'], "address": ['456 ', '457 ', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ['JACQUELINE', 'EDWARDS', '01/06/1951'], "address": ['461 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mrs", "Female", "British", "Widow(er)"], "ccj": False, "phone": False},
    {"name": ['D', 'GUEST', '01/12/1978'], "address": ['470 ', '471 ', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": False, "phone": False},
    {"name": ['HATTIE ', 'GUEST', '01/06/1958'], "address": ['471 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mrs", "Female", "British", "Widow(er)"], "ccj": False, "phone": False},
    {"name": ['PAUL ', 'BIRKINSHAW ', '01/07/1958'], "address": ['485 ', '', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Single"], "ccj": False, "phone": False},
    {"name": ['LESLIE ', 'DANIELS', '01/09/1964'], "address": ['486 ', '487 ', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Miss", "Female", "British", "Civil Partnership"], "ccj": False, "phone": False},
    {"name": ['E ', 'SWANN ', '01/05/1975'], "address": ['489 ', '488 ', ''], "bank": ['56-00-36', '40308669'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": False, "phone": False},
    {"name": ['Dian', 'Tamdy', '01/11/1965'], "address": ['27 ', '26 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Single"], "ccj": True, "phone": False},
    {"name": ['LINDSAY ', 'NAGY ', '01/07/1970'], "address": ['35 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Widow(er)"], "ccj": True, "phone": False},
    {"name": ['MOHAMMED ', 'BUTLER', '01/04/1956'], "address": ['42 ', '43 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['MUSHTAQ ', 'PICKARD', '01/01/1958'], "address": ['44 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": False, "phone": False},
    {"name": ['SHARON ', 'DRYDEN', '01/06/1973'], "address": ['54 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['CHRISTOPHER ', 'DRYDEN', '01/03/1974'], "address": ['55 ', '54 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": True, "phone": False},
    {"name": ['ELIZABETH ', 'Edwards', '01/04/1948'], "address": ['62 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": True, "phone": False},
    {"name": [' GEORGE', 'TYSOE', '01/01/1970'], "address": ['82 ', '81 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": True, "phone": False},
    {"name": ['ANITA ', 'WALTON', '01/04/1957'], "address": ['119 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Miss", "Female", "British", "Separated"], "ccj": True, "phone": False},
    {"name": ['ROY ', 'GEESON', '01/04/1950'], "address": ['137 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Civil Partnership"], "ccj": True, "phone": True},
    {"name": ['DAVID ', 'BROWN', '01/05/1964'], "address": ['220 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Divorced"], "ccj": True, "phone": False},
    {"name": ['FLORENCE ', 'ARCHER', '01/01/1936'], "address": ['218 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Miss", "Female", "British", "Widow(er)"], "ccj": True, "phone": False},
    {"name": ['PAM ', 'HEMINGWAY', '01/08/1955'], "address": ['263 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['MICK ', 'JOHNSON', '01/11/1941'], "address": ['267 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['PHILIP ', 'WILLIAMS', '01/12/1969'], "address": ['270 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Co-habiting"], "ccj": True, "phone": False},
    {"name": ['MICHAEL ', 'GARRAT', '01/09/1965'], "address": ['301 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Single"], "ccj": True, "phone": True},
    {"name": ['P', 'CLARKSON', '01/04/1969'], "address": ['309 ', '312 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['LYN ', 'SCOTT', '01/07/1970'], "address": ['316 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Ms", "Female", "British", "Divorced"], "ccj": True, "phone": False},
    {"name": ['MARK ', 'PARKES', '01/04/1961'], "address": ['318 ', '319 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ['SANDRA ', 'CLARKE', '01/01/1952'], "address": ['464 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mrs", "Female", "British", "Co-habiting"], "ccj": True, "phone": True},
    {"name": ['Martin ', 'Wesley ', '01/11/1969'], "address": ['505 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['PHIL ', 'ALDRIDGE ', '01/03/1952'], "address": ['521 ', '520 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['D ', 'LINDLEY ', '01/08/1952'], "address": ['540 ', '', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mrs", "Female", "British", "Married"], "ccj": False, "phone": True},
    {"name": ['KEVIN ', 'HARDCASTLE ', '01/06/1960'], "address": ['425 ', '424 ', ''], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ["JOHN ", "WALES", "01/04/1959"], "address": ["THE OLD VICARAGE", "12 ", "QUARRY HOUSE"],
     "bank": ['56-00-36', '57607230'], "details": ["Mr", "Male", "British", "Married"], "ccj": True, "phone": False},
    {"name": ["ELIZABETH ", "COLLIER", "01/04/1959"], "address": ["THE OAKS", "563 ", ""],
     "bank": ['56-00-36', '57607230'], "details": ["Mrs", "Female", "British", "Married"], "ccj": False,
     "phone": False},
    {"name": ["AMANDA", "SHIRT", "01/09/1967"], "address": ["THE NEST", "", ""], "bank": ['56-00-36', '57607230'],
     "details": ["Mrs", "Female", "British", "Married"], "ccj": True, "phone": False},
    {"name": ["KEN", "LINDEN", "01/02/1965"], "address": ["THE GARDNERS COTTAGE RUSHWOOD", "", ""],
     "bank": ['56-00-36', '57607230'], "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ["CAROL", "MAERRITT", "01/05/1959"], "address": ["SHIRE BARN", "High Trees", "Moorfields"],
     "bank": ['56-00-36', '57607230'], "details": ["Mrs", "Female", "British", "Married"], "ccj": False,
     "phone": False},
    {"name": ["ROY", "JACQUES", "01/09/1942"], "address": ["THE FIVE KILNS", "", ""], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": True},
    {"name": ["ALAN", "GLOVER ", "01/09/1969"], "address": ["TENBY", "389 ", "390 "], "bank": ['56-00-36', '57607230'],
     "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False},
    {"name": ["SUSAN", "TAYLOR ", "01/01/1943"], "address": ["PICKENHAM HOUSE", "Glenhurst Lodge", ""],
     "bank": ['56-00-36', '57607230'], "details": ["Mrs", "Female", "British", "Married"], "ccj": False,
     "phone": False},
    {"name": ["JENNIE", "FLEETWOOD ", "/07/1950"], "address": ["LLWYN ONN", "", ""], "bank": ['56-00-36', '57607230'],
     "details": ["Mrs", "Female", "British", "Married"], "ccj": False, "phone": True},
    {"name": ["SUE ", "BROWN ", "01/03/1950"], "address": ["LITTLECOTE", "448", ""], "bank": ['56-00-36', '57607230'],
     "details": ["Mrs", "Female", "British", "Married"], "ccj": False, "phone": True},
    {"name": ["SUSAN", "TAYLOR ", "01/01/1943"], "address": ["GLENHURST LODGE ", "Pickenham House", ""],
     "bank": ['56-00-36', '57607230'], "details": ["Mrs", "Female", "British", "Married"], "ccj": False, "phone": True},
    {"name": ["STEPHEN", "STOMER", "01/01/1960"], "address": ["FLATTS", "Tree Tops", ""],
     "bank": ['56-00-36', '57607230'], "details": ["Mr", "Male", "British", "Married"], "ccj": False, "phone": False}
]

import random


class User(object):
    def __init__(self, report=1, ccj_value=False, phone_value=False, ):

        def user_index():
            """ func that returns the index of the object that meets the initializator variable values(requirements)
            :return: int
            """
            index = 0
            while True:
                index = random.randint(0, (mass.__len__() - 1))
                if mass[index]["ccj"] == ccj_value and mass[index]["phone"] == phone_value:
                    break
            return index

        self.selector = user_index()
        self.name = mass[self.selector]["name"][0]
        self.surename = mass[self.selector]["name"][1]
        self.birthdate = mass[self.selector]["name"][2]
        self.address1 = mass[self.selector]["address"][0]
        self.address2 = mass[self.selector]["address"][1]
        self.address3 = mass[self.selector]["address"][2]
        self.sort_code = mass[self.selector]["bank"][0]
        self.account = mass[self.selector]["bank"][1]
        self.title = mass[self.selector]["details"][0]
        self.sex = mass[self.selector]["details"][1]
        self.origin = mass[self.selector]["details"][2]
        self.status = mass[self.selector]["details"][3]
        self.report_type = report
        self.payinginadvance = False
        self.hasemail = True
        self.incomeverification_required = True
        self.rentshare = None


    @report_type.setter
    def set_report_type(self, value):
        self.report_type = value


if __name__ == '__main__':
    x = User()
print(x.__dict__)
