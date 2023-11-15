import dataclasses
import constants


@dataclasses.dataclass
class Message:
    network: str = constants.MESSAGE_NETWORK


message = Message()
