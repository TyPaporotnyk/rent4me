from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Customer:
    id: int | None = field(default=None, kw_only=True)
    username: str
    created_at: datetime
