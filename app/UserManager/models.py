
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(128), unique=True, nullable=False)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    # is_authenticated = db.Column(db.Boolean, default=True)
    # is_active = db.Column(db.Boolean, default=True)
    # is_anonymous = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @staticmethod
    def create(data):
        user = User(email=data.get('email'),
                    username=data.get('username'),
                    password=data.get('password'),
                    first_name=data.get('first_name'),
                    last_name=data.get('last_name')
                    )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(user_id=None, email=None, username=None):
        if user_id is not None:
            return User.query.get(user_id)
        elif email is not None:
            return User.query.filter_by(email=email).first()
        elif username is not None:
            return User.query.filter_by(username=username).first()
        raise AttributeError('AttributesNotTrue')

    def to_dict(self):
        data = self.__dict__
        del data['_sa_instance_state']
        return data

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    # def is_active(self):
    #     return True
    #
    #
    # def is_authenticated(self):
    #     return True
    #
    #
    # def is_anonymous(self):
    #     return False

    def get_id(self):
        try:
            return self.id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

