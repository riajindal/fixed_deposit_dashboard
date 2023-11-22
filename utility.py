from bank import Bank
import os
import sys
from definition import ROOT_PATH

PROJECT_ROOT = os.path.dirname(os.path.abspath(ROOT_PATH))

bank_list_priv = [Bank(r'data_extraction/hdfc_slabs.csv', 'HDFC'),
                  Bank(r'data_extraction/kotak_slabs.csv', 'KOTAK'),
                  Bank(r'data_extraction/icici_slabs.csv', 'ICICI'),
                  Bank(r'data_extraction/axis_slabs.csv', 'AXIS'),
                  Bank(r'data_extraction/idfc_slabs.csv', 'IDFC')]

bank_list_public = [Bank(r'data_extraction/sbi_slabs.csv', 'SBI'),
                    Bank(r'data_extraction/pnb_slabs.csv', 'PNB'),
                    Bank(r'data_extraction/bob_slabs.csv', 'BOB'),
                    Bank(r'data_extraction/canara_slabs.csv', 'CANARA'),
                    Bank(r'data_extraction/union_slabs.csv', 'UNION'),
                    Bank(r'data_extraction/hsbc_slabs.csv', 'HSBC')]

master = bank_list_priv + bank_list_public

# Adjust index to fix error in Bank of Baroda script
data = master[7].df
data.loc[7, 'Min Value'] = 271
data.loc[7, 'Max Value'] = 365


# bank_dict = {
#     'HDFC': Bank('https://www.paisabazaar.com/fixed-deposit/hdfc-fd-rates/'),
#     'AXIS': Bank('https://www.paisabazaar.com/fixed-deposit/axis-bank-fd-rates/'),
#     'ICICI': Bank('https://www.paisabazaar.com/fixed-deposit/icici-bank-fd-rates/'),
#     'IDFC': Bank('https://www.paisabazaar.com/idfc-bank/fixed-deposits/'),
#         }
