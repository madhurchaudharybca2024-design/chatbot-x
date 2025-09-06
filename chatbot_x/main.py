from flask import Flask, request, render_template_string
from chatbot_x.chat_engine import ChatEngine

app = Flask(__name__)
bot = ChatEngine()

HTML_TEMPLATE = """
<!doctype html>
<title>ChatBot-X</title>
<h2>ChatBot-X: Advanced NLP Customer Support Chatbot</h2>
<div id="chatbox"></div>
<form method="post" id="chatForm">
  <input type="text" name="message" id="message" autofocus autocomplete="off"/>
  <input type="submit" value="Send"/>
</form>
<script>
document.getElementById('chatForm').onsubmit = function(e){
  e.preventDefault();
  var msg = document.getElementById('message').value;
  fetch('/', {
    method:'POST',
    headers:{'Content-Type':'application/x-www-form-urlencoded'},
    body:'message='+encodeURIComponent(msg)
  }).then(res=>res.text()).then(html=>{
    document.body.innerHTML = html;
  });
}
</script>
{% if user_msg %}
<p><b>You:</b> {{ user_msg }}</p>
<p><b>ChatBot-X:</b> {{ bot_response }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    user_msg = None
    bot_response = None
    if request.method == "POST":
        user_msg = request.form["message"]
        bot_response = bot.get_response(user_msg)
    return render_template_string(HTML_TEMPLATE, user_msg=user_msg, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)