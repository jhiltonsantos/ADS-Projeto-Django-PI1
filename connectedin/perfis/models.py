from django.db import models


class Perfil(object):
    def __init__(self, id = 0, name='', email='', telephone='', name_comp='',):
        self.id = id
        self.name = name
        self.email = email
        self.telephone = telephone
        self.name_comp = name_comp
