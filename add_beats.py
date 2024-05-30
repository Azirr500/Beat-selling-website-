from app import app
from extensions import db
from models import Beat

def add_beats():
    with app.app_context():
        beats = [
            {"title": "Beat 1", "filename": "millions.mp3", "price": 1.99},
            {"title": "Beat 2", "filename": "spaceyuntaggedmp3.mp3", "price": 2.99},
            {"title": "Beat 3", "filename": "vit.mp3", "price": 1.49},
        ]

        for beat in beats:
            new_beat = Beat(title=beat["title"], filename=beat["filename"], price=beat["price"])
            db.session.add(new_beat)
        db.session.commit()

if __name__ == '__main__':
    add_beats()
