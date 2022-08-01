# from src.category.domain.entities import Category
from datetime import datetime
from dataclasses import dataclass, field
import uuid

from typing import Optional

# KW_ONLY=True -> obriga utilizacao de parametros nomeados


@dataclass(kw_only=True)
class Category:

    id: uuid.UUID = field(default_factory=lambda: uuid.uuid4())
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now())
