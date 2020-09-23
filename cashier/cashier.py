import os
import json
import requests
import logging

from jsonschema import validate

logging.basicConfig(filename='cashier.log', level=logging.DEBUG)

class Cashier():
    """ 
    This application have the checkout responbility.
    """
    def __init__(self, payload=None):
        self.payload = payload
        """
        The payload can't be empty and need to be a dict
        """
        if not self.payload:
            raise Exception('Payload can not be empty')
        if not type(self.payload) == dict:
            raise Exception('Payload need to be a dict')

    def _get_data_from_request(self, response, data):
        """
        This function will make sure that the key it's sending already exist in response
        """
        if not data in response.keys():
            raise Exception('Error in request data')

        return response[data]

    def _get_provider_url(self):
        url = os.environ.get('PROVIDER_URL')
        if not url:
            raise Exception('Error in provider url')
        return url


    def request_data(self):
        try:

            logging.info('[Cashier.request_data]')
            response = requests.request('GET', self._get_provider_url())

            if response.status_code != 200:
                raise Exception('Error in request provider data')

            return json.loads(response.text)

        except Exception as error:
            logging.error(error)
            raise error
            
        
    @property
    def is_valid(self):

        response = self.request_data()

        url = self._get_data_from_request(response, 'url')
        auth = self._get_data_from_request(response, 'auth')
        schema = self._get_data_from_request(response, 'schema')

        """
        It's important to make sure that the parameters have been informed
        """
        if not url or not schema or not self.payload:
            raise Exception('Some param is missing')

        try:
            logging.info(f"[Cashier.is_valid - {url} - {self.payload} - {schema}]")
            validate(instance=self.payload, schema=schema)
        except Exception as error:
            """
            Get any exception about json schema validate
            """
            logging.error(error)
            raise error
        """
        For all cases, if don't raised a expection
        """
        return True

    def create_checkout(self, url):
        """
        The ``url`` is the provider's url
        The ``payload`` is the data that the provider expects for the request
        """
        logging.info('[Cashier.create_checkout]')
        response = requests.request('POST', url=url, payload=self.payload)

        if response.status_code == 200:
            logging.info('[Cashier.done]')
            return response.text
        else:
            logging.info('[Cashier.fail]')
            raise Exception('Checkout fail')

