from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timedelta
from uuid import uuid4 # パスワード発行の際に便利な機能


@login_manager.user_loader # ログインが必要なページの行くたびに呼び出される
def load_user(user_id):
  return User.query.get(user_id)


class User(UserMixin, db.Model):

  __tablename__ = 'users'

id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(64), index=True)
email = db.Column(db.String(64), unique=True, index=True) # emailは必ずユニーク
password = db.Column(db.String(128), default=generate_password_hash('snsflaskapp'))
picture_path = db.Column(db.Text)
is_active = db.Column(db.Boolean, unique=False, default=False)
create_at = db.Column(db.Datetime, default=datetime.now)
update_at = db.Column(db.Datetime, default=datetime.now)


class PasswordResetToken(db.Model):

  __tablename__ = 'password_reset_token'

  id = db.Column(db.Integer, primary_key=True)
  token = db.Column(db.String(64), unique=True, index=True, default=str(uuid4))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  expire_at = db.Column(db.Datatime, default=datetime.now)
  create_at = db.Column(db.Datetime, default=datetime.now)
  update_at = db.Column(db.Datetime, default=datetime.now)