from decouple import config

# Twilio
ACCOUNT_SID: str = config('ACCOUNT_SID')
AUTH_TOKEN: str = config('AUTH_TOKEN')
FROM: str = config('FROM', default='+16083365018')

# Messages
REPLACE_DEVICE: str = config('REPLACE_DEVICE', default='<device_id>')
MESSAGE_NETWORK: str = config('MESSAGE_NETWORK')
