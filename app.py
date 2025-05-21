from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    print("✅ Twilio reached the Flask bot!")

    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    msg.body("Hi! I am DanaDone! Your Daily Update Bot. What did you do today that you want to count or keep track of?")

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)

