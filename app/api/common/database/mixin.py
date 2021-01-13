from . import db
from flask_login import UserMixin

text_type = str

class BaseModelMixin(object):
    def save(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()

    def get_all(self, **kwargs):
        return self.query.filter_by(**kwargs).all()
    
    def get_by_id(self, id):
        return self.query.get(id)


class UserMixin(BaseModelMixin, UserMixin):
    
    def get_id(self):
        try:
            return text_type(self.PERSON_ID)
        except AttributeError:
            raise NotImplementedError('No `PERSON_ID` attribute - override `get_id`')
    