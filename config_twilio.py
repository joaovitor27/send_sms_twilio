import dataclasses

from twilio.rest import Client
from twilio.rest.api.v2010.account.message import MessageInstance

from constants import ACCOUNT_SID, AUTH_TOKEN, FROM


@dataclasses.dataclass
class ConfigTwilio:
    account_sid: str = ACCOUNT_SID
    auth_token: str = AUTH_TOKEN
    from_: str = FROM
    to: str = None

    def init_twilio(self: 'ConfigTwilio') -> Client:
        return Client(self.account_sid, self.auth_token)

    def send_message(self: 'ConfigTwilio', message_: str) -> MessageInstance:
        return self.init_twilio().messages.create(from_=self.from_, body=message_, to=self.to)

    def with_to(self: 'ConfigTwilio', to: str) -> 'ConfigTwilio':
        self.to = to
        return self

    def __call__(self: 'ConfigTwilio', message: str) -> MessageInstance:
        return self.send_message(message)
