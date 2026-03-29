import uuid
import datetime
from dataclasses import dataclass

@dataclass
class A2AMessage:

    message_id:str
    sender:str
    receiver:str
    task:str
    timestamp:str
    context:dict


def create_message(sender,receiver,task,context=None):

    return A2AMessage(
        message_id=str(uuid.uuid4()),
        sender=sender,
        receiver=receiver,
        task=task,
        timestamp=str(datetime.datetime.now()),
        context=context or {}
    )
