import requests

def send_sms(customer):
    url = 'https://api.sandbox.africastalking.com/version1/messaging'
    headers = {
        'apiKey': 'eff9f0a39a91c7d999e9c01bb6230374413292d4f6718a11aa473b9020dff921',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'username': 'sandbox',
        'to': customer.phone,  # assuming customer has a phone attribute
        'message': f'Hello {customer.name}, your order has been placed successfully!',
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()
