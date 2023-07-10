# twilio - integração com SMS

from twilio.rest import Client

# Autenticador SMS
account_sid = 'ACfeaa5b7f5889a368e238fa098f84885c'  # os.environ['TWILIO_ACCOUNT_SID']
auth_token = 'cb9e9d03636820e5fd86b962cc66a154'  # os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
fone_from_sms = '+12345012669'
fone_from_whatsapp = 'whatsapp:+14155238886'


class Message:

    def SendSms(self, fone_to):
        message = client.messages.create(
            body=self[:1500],
            from_=fone_from_sms,
            to=fone_to
            )

        return message

    def SendWhatsApp(self, fone_to):
        message = client.messages.create(
            body=self[:1500],
            from_=fone_from_whatsapp,
            to=f'whatsapp:{fone_to}'
        )

        return message
