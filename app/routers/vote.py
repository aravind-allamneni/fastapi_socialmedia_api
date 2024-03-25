from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import oauth2
from .. import models
from .. import schemas
from ..database import get_db


router = APIRouter(tags=["Votes"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(
    vote: schemas.VoteIn,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {vote.post_id} not found",
        )
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )
    already_voted = vote_query.first()
    if vote.vote_dir == 1:
        if already_voted:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User: {current_user.id} has already upvoted on post: {vote.post_id}",
            )
        else:
            new_vote = models.Vote(user_id=current_user.id, post_id=vote.post_id)
            db.add(new_vote)
            db.commit()
            return {"message": "successfully added vote"}
    else:
        if not already_voted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist"
            )
        else:
            vote_query.delete(synchronize_session=False)
            db.commit()
            return {"message": "successfully deleted vote"}
