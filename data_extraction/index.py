# DATA EXTRACTION DRIVER FILE
from extract_slabs import create_csv

# banks = icici, hdfc, idfc, axis
# store in dictionary: {'bank name': 'url'}
urls = {
    'HDFC': 'https://www.paisabazaar.com/fixed-deposit/hdfc-fd-rates/',
    'AXIS': 'https://www.paisabazaar.com/fixed-deposit/axis-bank-fd-rates/',
    'ICICI': 'https://www.paisabazaar.com/fixed-deposit/icici-bank-fd-rates/',
    'IDFC': 'https://www.paisabazaar.com/idfc-bank/fixed-deposits/',
        }

for key, value in urls.items():
    create_csv(key, value)
