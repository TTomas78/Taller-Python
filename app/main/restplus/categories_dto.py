from flask_restplus import Namespace
#from flask_restplus import fields


class CategoriesDto():
    api = Namespace('Categories',
                    description='Categories related operations',
                    path='/')
