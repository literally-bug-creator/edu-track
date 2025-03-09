from sqlalchemy.orm import Mapped, mapped_column, declarative_base

SQLBase = declarative_base()


class Base(SQLBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
