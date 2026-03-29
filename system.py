from agents import FAQAgent,BillingAgent,TechnicalAgent
from a2a_protocol import create_message


class A2ASystem:

    def __init__(self):

        self.agents={
            "faq":FAQAgent(),
            "billing":BillingAgent(),
            "tech":TechnicalAgent()
        }


    def triage(self,query):

        q=query.lower()

        if "payment" in q or "refund" in q:
            return "billing"

        if "error" in q or "bug" in q:
            return "tech"

        return "faq"


    def process(self,query):

        first_agent=self.triage(query)

        message=create_message(
            "customer",
            first_agent,
            query
        )

        while message.receiver!="customer":

            agent=self.agents.get(message.receiver)

            message=agent.handle(message)

        return message.task
