from sqlalchemy.orm import Session
from src.posts import schemas
from src.posts import repository, schemas


def create_post(repo: repository.PostRepository, post_in: schemas.PostCreate):
    # Business rule: don’t allow "spam" in title
    if "spam" in post_in.title.lower():
        raise ValueError("Spam is not allowed")
    return repo.create(post_in)

def list_posts(repo: repository.PostRepository):
    posts = repo.list_all()
    # Business rule: filter hidden posts
    return [p for p in posts if p.is_active ]

# OR if using FastAPI Depends in router:
# def create_post(repo: PostRepository = Depends(get_post_repo), post_in: schemas.PostCreate):
#     return repo.create(post_in)
