from flask import Flask, Blueprint, render_template, redirect, url_for, request, jsonify
from apps.info.forms import TalkForm
from apps.app import db
from apps.info.models import ChatMessage  # ChatMessage 모델 추가

info = Blueprint(
    "info",
    __name__,
    template_folder="templates",
    static_folder="static"
)

@info.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 폼 처리 로직을 여기에 추가
        return redirect(url_for('info.friends'))
    return render_template("info/index.html")

@info.route('/friends', methods=['GET', 'POST'])
def friends():
    return render_template('info/friends.html')

@info.route('/chats', methods=['GET', 'POST'])
def chats():
    # 모든 채팅 내용을 가져와서 전송
    messages = ChatMessage.query.all()
    return render_template('info/chats.html', messages=messages)

@info.route('/chat', methods=['GET', 'POST'])
def chatting():
    return render_template('info/chat.html')

@info.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']

    # 여기서 데이터베이스에 저장하는 로직을 추가할 수 있음
    new_message = ChatMessage(message=message, sender='User')  # 예시로 'User'를 sender로 설정
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': message})

@info.route('/get-messages', methods=['GET'])
def get_messages():
    messages = ChatMessage.query.all()
    message_list = [{'sender': message.sender, 'message': message.clean_message} for message in messages]
    return jsonify({'messages': message_list})

app = Flask(__name__)
app.register_blueprint(info, url_prefix='')  # url_prefix=''으로 설정

if __name__ == '__main__':
    app.run()
