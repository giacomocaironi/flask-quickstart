from app import db

tag_post_table = db.Table(
    "tag_post",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    content = db.Column(db.String)
    category_id = db.Column(db.ForeignKey("category.id"))

    def __repr__(self):
        return f"{self.title}"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    posts = db.relationship("Post", backref="category", lazy="dynamic")

    def __repr__(self):
        return f"{self.name}"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    posts = db.relationship(
        "Post", secondary=tag_post_table, backref="tags", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.name}"
