from flask_restplus import Api

from .cashier import api as cashier

api = Api(title='API REST', version='1.0', description='A sample application that create a checkout')

api.add_namespace(cashier)