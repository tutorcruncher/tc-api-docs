import hashlib, hmac

HMAC_PRIVATE_KEY = 'YOUR_PRIVATE_API_KEY'

def webhook_view(request):
    payload = request.body
    header_signature = request.META['Webhook-Signature']
    assert hmac.new(HMAC_PRIVATE_KEY.encode(), payload, hashlib.sha256).hexdigest() == header_signature
