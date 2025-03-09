from . import Base
from sqlalchemy.orm import Mapped, mapped_column
    

class Units(Base):
    __tablename__ = "units"
    
    name: Mapped[str] = mapped_column()