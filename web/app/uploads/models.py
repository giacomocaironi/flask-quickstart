from app import db
from app import images, documents


class Image(db.Model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    filename = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return self.name

    @property
    def url(self):
        return images.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return images.path(self.filename)


class Document(db.Model):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    filename = db.Column(db.String(128), unique=True)

    def __repr__(self):
        return self.name

    @property
    def url(self):
        return documents.url(self.filename)

    @property
    def filepath(self):
        if self.filename is None:
            return
        return documents.path(self.filename)
