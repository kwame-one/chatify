import uuid
from datetime import datetime
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select, desc, update


class BaseRepository:
    def __init__(self, model, db_session):
        self.model = model
        self.db_session = db_session

    def find_all(self, query=None):
        db_query = select(self.model).where(self.model.deleted_at.is_(None)).order_by(desc(self.model.id))
        return paginate(self.db_session, db_query)

    def find(self, id):
        return self.db_session.scalars(select(self.model)
                                       .where(self.model.deleted_at.is_(None))
                                       .where(self.model.id == id)).first()

    def update(self, id, data):
        self.db_session.execute(update(self.model)
                                .where(self.model.deleted_at.is_(None))
                                .where(self.model.id == id).values(**data))
        self.db_session.commit()
        return self.find(id)

    def store(self, data):
        data['id'] = str(uuid.uuid4())
        resource = self.model(**data)
        self.db_session.add(resource)
        self.db_session.commit()
        self.db_session.refresh(resource)
        return resource

    def delete(self, id):
        self.db_session.execute(update(self.model)
                                .where(self.model.deleted_at.is_(None))
                                .where(self.model.id == id)
                                .values(deleted_at=datetime.now()))
        self.db_session.commit()
