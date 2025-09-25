from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.posts import schemas, service, repository

router = APIRouter(prefix="/posts", tags=["posts"])

def get_repo(db: Session = Depends(get_db)):
    """
        Provides a fresh repository instance for each request.

        Flow:
        1. get_db() yields a new SQLAlchemy session
        2. PostRepository(db) is created with that session
        3. Repo is passed to router endpoint as argument
        """
    return repository.PostRepository(db)

# router.py
@router.post("/", response_model=schemas.PostOut)
def create_post(
                post: schemas.PostCreate,  # incoming request body validated against PostCreate
                repo: repository.PostRepository = Depends(get_repo)
            ):
    """
       Endpoint: POST /posts/
       PostCreate = request validation, PostOut = response serialization.

       Flow when request hits:
       1. FastAPI parses request body into PostCreate (Pydantic validates types)
       2. get_repo() is called to inject repository
       3. Router calls service.create_post(repo, post)
       4. Repository persists the Post in DB (SQLAlchemy session)
       5. SQLAlchemy Post object is returned
       6. FastAPI converts SQLAlchemy object to PostOut (Pydantic, orm_mode=True)
       7. JSON response is sent to client
       """
    return service.create_post(repo, post)



@router.get("/", response_model=list[schemas.PostOut])
def list_posts(repo: repository.PostRepository = Depends(get_repo)):
    return service.list_posts(repo)
