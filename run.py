#!/usr/bin/env python
import os
import sys
from app import create_app, db
from app.models import Post, Comment

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Post': Post,
        'Comment': Comment
    }

@app.cli.command()
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized!')

@app.cli.command()
def seed_db():
    """Seed the database with sample data."""
    print('Use seed_simplified.py to seed the database')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_ENV') == 'development')
