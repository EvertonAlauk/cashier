import json
import requests
import logging

from jsonschema import validate

logging.basicConfig(filename='cashier.log', level=logging.DEBUG)

class Cashier(object):
    """ 
    This application have the checkout responbility.
    """
    def __init__(cls, url=None, schema=None, payload=None):
        cls.url = url
        cls.schema = schema
        cls.payload = payload

    def is_valid(cls):
        if not cls.url or not cls.schema or not cls.payload:
            logging.warning('Some param is missing')
            raise Exception('Some param is missing')
        return cls

    def validate_schema(cls):
        try:
            logging.info('Schema validate')
            return validate(instance=cls.payload, schema=cls.schema)
        except Exception as error:
            """
            Get any exception about json schema validate
            """
            logging.warning(error.message)
            raise Exception(error.message)

    def create_checkout(cls):
        """
        The ``url`` is the provider's url
        The ``payload`` is the data that the provider expects for the request
        """
        logging.info('Create a checkout')
        response = requests.request('POST', url=cls.url, payload=cls.payload)

        if request.status_code == 200:
            logging.info('Checkout done')
            return json.loads(request.text)
        else:
            logging.info('Checkout failure')
            raise Exception('Checkout failure')
