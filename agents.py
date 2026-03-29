from groq import Groq
from a2a_protocol import create_message

MODEL="llama-3.3-70b-versatile"

client=Groq()


class FAQAgent:

    name="faq"

    faq={
        "return":"You can return items within 30 days.",
        "refund":"Refund processed within 5 days.",
        "shipping":"Shipping takes 3-5 business days."
    }

    def handle(self,msg):

        query=msg.task.lower()

        for k in self.faq:
            if k in query:
                return create_message(
                    "faq",
                    "customer",
                    self.faq[k]
                )

        return create_message(
            "faq",
            "tech",
            query
        )


class BillingAgent:

    name="billing"

    def handle(self,msg):

        query=msg.task.lower()

        if "refund" in query:
            answer="Refunds are processed within 5-7 business days."

        elif "payment" in query:
            answer="We accept cards, PayPal, and bank transfers."

        else:
            answer="Please clarify your billing question."

        return create_message(
            "billing",
            "customer",
            answer
        )


class TechnicalAgent:

    name="tech"

    def handle(self,msg):

        prompt=f"""
Customer problem:
{msg.task}

Provide troubleshooting steps.
"""

        r=client.chat.completions.create(
            model=MODEL,
            messages=[{"role":"user","content":prompt}]
        )

        answer=r.choices[0].message.content

        return create_message(
            "tech",
            "customer",
            answer
        )
