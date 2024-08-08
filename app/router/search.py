from fastapi import APIRouter, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import text, func
import sqlalchemy
from typing import List, Optional, Literal
from pydantic import BaseModel
from .. import models, schemas, oauth2
from ..database import get_db, engine
from ..config import settings

router = APIRouter(
    prefix="/search",
    tags=['Search']
)


class Schema(BaseModel):
    schema: Literal['canada', 'australia', 'mexico', 'united_states_of_america'] = 'united_states_of_america'




@router.get("/" ,response_model=List[schemas.ResultsBase]) 
def search_table(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), q: Optional[str] = "", limit: int = 10, skip: int = 0):
    
    query = """
            SELECT id, title, url, content FROM public.supersift_engine
            WHERE ts @@ websearch_to_tsquery('english', :search_term)
            LIMIT :limit OFFSET :skip;
            """
    
    search = db.execute(text(query), {'search_term':q, 'limit' :limit,'skip':skip}).fetchall()
    if not search:
        raise HTTPException(status_code=404, detail=f"Your search '{q}' was not found")

    return search

