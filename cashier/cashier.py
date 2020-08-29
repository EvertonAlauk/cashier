import logging
import requests

logging.basicConfig(
    filename='cashier.log', level=logging.DEBUG
    )

class Cashier:
    """ 
    This application have the checkout responbility.
    """
    def __init__(self, url=None, schema=None, payload=None):
        self.url = url
        self.schema = schema
        self.payload = payload

    def is_valid(self):
        """
        check if the three arguments are passed
        """
        if not self.url:
            logging.debug('URL is missing')
            raise Exception('URL is missing')
        if not self.schema:
            logging.debug('Schema is missing')
            raise Exception('Schema is missing')
        if not self.payload:
            logging.debug('Payload is missing')
            raise Exception('Payload is missing')
        return True

if __name__ == "__main__":

    cashier = Cashier()
    if cashier.is_valid():
        logging.debug('OK')
    logging.debug('NOK')