"""Seed file to make sample data for users db."""

from models import User, db


# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
Agent = User(
    first_name='Agent', 
    last_name='Smith',
    image_url="https://upload.wikimedia.org/wikipedia/en/1/1f/Agent_Smith_%28The_Matrix_series_character%29.jpg")
Joseph = User(
    first_name='Joseph', 
    last_name='Smith',
    image_url="https://newsroom.churchofjesuschrist.org/media/orig/Joseph-Smith-prophet.jpg")
Will = User(
    first_name='Will', 
    last_name='Smith',
    image_url="https://m.media-amazon.com/images/M/MV5BNTczMzk1MjU1MV5BMl5BanBnXkFtZTcwNDk2MzAyMg@@._V1_FMjpg_UX1000_.jpg")

# Add new objects to session, so they'll persist
db.session.add(Agent)
db.session.add(Joseph)
db.session.add(Will)

# Commit--otherwise, this never gets saved!
db.session.commit()
