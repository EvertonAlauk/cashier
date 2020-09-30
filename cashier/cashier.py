import os
import json
import requests
import logging

from jsonschema import validate
from jsonschema import ValidationError as JSONSchemaValidationError

logging.basicConfig(filename='cashier.log', level=logging.INFO)

class Cashier():
    """ 
    This application have the checkout responbility.
    """
    def __init__(self, payload=None):
        """
        The payload can't be empty and need to be a dict
        """
        self.payload = payload

        if not self.payload:
            raise Exception('Payload can not be empty')
        if not type(self.payload) == dict:
            raise Exception('Payload need to be a dict')

    @classmethod
    def _get_data_from_request(self, response, data):

        if not data in response.keys():
            logging.error('Error in request data')
            raise Exception('Error in request data')

        return response[data]

    @classmethod
    def _get_provider_url(self):

        url = os.environ.get('PROVIDER_URL')
        if not url:
            logging.error('Error in provider url')
            raise Exception('Error in provider url')

        return url

    def request_data(self):
        logging.info('Cashier.request_data')

        response = requests.get(
            url=self._get_provider_url(),
            headers={
                "Content-Type": "application/json"
            }
        )
        if response.status_code != 200:
            logging.error('Error in request provider data')
            raise Exception('Error in request provider data')
            
        try:
            return json.loads(response.content)
        except json.decoder.JSONDecodeError:
            logging.error('Error in JSON loads')
            raise Exception('Error in JSON loads')
            
        
    @property
    def is_valid(self):

        response = self.request_data()
        
        url = self._get_data_from_request(response, 'url')
        auth = self._get_data_from_request(response, 'auth')
        schema = self._get_data_from_request(response, 'schema')

        if not url or not schema or not self.payload:
            raise Exception('Some param is missing')

        try:
            logging.info("Cashier.is_valid")
            validate(instance=self.payload, schema=schema)
        except JSONSchemaValidationError as error:
            logging.error(error)
            raise Exception(error)

        return True

    def create_checkout(self, url):

        logging.info('Cashier.create_checkout')
        response = requests.request('POST', url=url, payload=self.payload)

        if response.status_code == 200:
            logging.info('Cashier.done')
            return response.text
        else:
            logging.info('Cashier.fail')
            raise Exception('Checkout fail')