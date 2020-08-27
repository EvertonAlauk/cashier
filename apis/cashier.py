
from flask_restplus import Namespace
from flask_restplus import Resource

from cashier import cashier

api = Namespace('cashier', description='Methods')

@api.route('/')
class CashierAPI(Resource):
    def get(self):

        print(cashier)
        
        return 200, { "message": "OK" }