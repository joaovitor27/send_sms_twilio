import dataclasses
import constants


@dataclasses.dataclass
class Message:
    network: str = constants.MESSAGE_NETWORK
    event: str = constants.MESSAGE_EVENT
    shipping: str = constants.MESSAGE_SHIPPING


message = Message()
