from datetime import datetime
from apps.app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Talk(db.Model):
    __tablename__ = 'talk'
    id = db.Column(db.Integer, primary_key=True)
    chatlog = db.Column(db.String, index=True)

class ChatMessage(db.Model):
    __tablename__ = 'chat_message'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)
    sender = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def clean_message(self):
        return self.message[len("User: "):] if self.message.startswith("User: ") else self.message

    def __repr__(self):
        return f'<ChatMessage {self.id}>'
    