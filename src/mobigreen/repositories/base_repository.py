class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def get(self, id: int) -> T | None:
        return self.session.get(self.model, id)

    def get_all(self) -> list[T]:
        return self.session.query(self.model).all()

    def create(self, obj: T) -> T:
        self.session.add(obj)
        return obj

    def delete(self, obj: T) -> None:
        self.session.delete(obj)
