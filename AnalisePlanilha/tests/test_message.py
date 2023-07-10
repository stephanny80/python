from app.message import Message

def test_sms():
    message = Message.SendSms('test Sms', '+5534988989078')
    assert len(message.sid) > 10


def test_whatsapp():
    message = Message.SendWhatsApp('test WhatsApp', '+5534988989078')
    assert len(message.sid) > 10
