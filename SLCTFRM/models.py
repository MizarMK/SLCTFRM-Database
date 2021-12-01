from SLCTFRM import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_account(account_id):
    return Account.query.get(int(account_id))


class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    favTeamid = db.Column(db.String(3), nullable=True)
    favTeam = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"'{self.username}, {self.email}, {self.favTeam}'"
