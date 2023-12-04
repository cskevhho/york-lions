from ...models.rating import Rating
from ...extensions import db


def delete_all():
    ratings = Rating.query.all()

    if not Rating.query.all():
        return {"message": "No ratings to delete"}, 400
    for rating in ratings:
        db.session.delete(rating)

    db.session.commit()
    return {"message": "All ratings deleted successfully"}, 200

