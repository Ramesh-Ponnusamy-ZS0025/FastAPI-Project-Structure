from sqlalchemy.orm import Session
from src.posts import models, schemas

class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, post_in: schemas.PostCreate) -> models.Post:
        db_post = models.Post(**post_in.dict())
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return db_post

    def get_by_id(self, post_id: int):
        return self.db.query(models.Post).filter(models.Post.id == post_id).first()

    def list_all(self):
        return self.db.query(models.Post).all()

    def delete(self, post_id: int):
        row = self.db.query(models.Post).filter(models.Post.id == post_id).first()
        if row:
            self.db.delete(row)
            self.db.commit()
        return row
