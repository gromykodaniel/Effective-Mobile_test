class BookClass:

    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):

        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def from_input_to_dict(self) -> dict:

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict_to_object(data: dict) -> "Book":

        return BookClass(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )