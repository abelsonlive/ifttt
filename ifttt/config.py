import os

IFTTT_USERNAME = os.getenv('IFTTT_USERNAME')
IFTTT_PASSWORD = os.getenv('IFTTT_PASSWORD')
IFTTT_SERVER = os.getenv('IFTTT_IMAP_SERVER')
IFTTT_PORT = os.getenv('IFTTT_IMAP_PORT', 993)
IFTTT_DELIM = os.getenv('IFTTT_DELIM', '\|\|\|\|\|')