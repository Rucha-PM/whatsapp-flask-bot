from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg.lower() in ['hi', 'hello', 'hey']:
        msg.body("✨ Welcome to DanaDone – your daily simple habit tracker! What’s one thing you did today that you want to count?")
    else:
        msg.body(f"Good job! I’ll keep track of: “{incoming_msg}” 💪")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
