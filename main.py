from twilio.rest.api.v2010.account.message import MessageInstance

from config_twilio import ConfigTwilio
from constants import REPLACE_DEVICE
from messages import message

RECIPIENTS: list = [
    {'phone': '+5586995880950', 'device_id': '212121212'},
    {'phone': '+5586995880950', 'device_id': '454545455'},
    {'phone': '+5586995880950', 'device_id': '897978997'},
]

MESSAGE: str = message.network

for recipient in RECIPIENTS:
    send_message: callable(ConfigTwilio) = ConfigTwilio().with_to(recipient.get('phone'))
    result: MessageInstance = send_message(MESSAGE.replace(REPLACE_DEVICE, recipient.get('device_id')))
    print(result)
