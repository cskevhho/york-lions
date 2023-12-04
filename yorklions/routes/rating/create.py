from ...models.rating  import Rating
from ...extensions import db
from datetime import datetime

def create_rating(f_name, l_initial, rating, review_body, review_date):
    new_rating = Rating(
            f_name=f_name,
            l_initial=l_initial,
            rating=rating,
            review_body=review_body,
            review_date=datetime.now().strftime("%F-%R")
            )
    db.session.add(new_rating)
    db.session.commit()
    return {"message": f"Rating {new_rating.id} has been created successfully.", "new_rating_id": new_rating.id}, 200

def admin_create_rating(make, model, year, f_name, l_initial, rating, review_body, review_date):
    new_rating = Rating(
            make=make,
            model=model,
            year=year,
            f_name=f_name,
            l_initial=l_initial,
            rating=rating,
            review_body=review_body,
            review_date=datetime.now().strftime("%F-%R")
            )
    db.session.add(new_rating)
    db.session.commit()
    return {"message": f"Rating {new_rating.id} has been created successfully.", "new_rating_id": new_rating.id}, 200
