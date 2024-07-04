import json
from flask import Flask, request
import requests

app = Flask(__name__)

# إعدادات CallMeBot
api_key = '249127128021'
recipient_number = '8382879'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    order_id = data.get('order_id')
    customer_name = data.get('customer', {}).get('name')
    order_total = data.get('total')
    
    message_body = f'New Order Received!\nOrder: {data}\n'
    
    send_message(message_body)

    return 'Message sent', 200

def send_message(message):
    url = f'https://api.callmebot.com/whatsapp.php?phone={recipient_number}&text={message}&apikey={api_key}'
    response = requests.get(url)
    return response

if __name__ == '__main__':
    app.run(port=5000)