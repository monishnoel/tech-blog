#!/usr/bin/env python3
"""Seed the database with sample data"""

from app import create_app, db
from app.models import User, Post

app = create_app()

with app.app_context():
    # Create demo user if it doesn't exist
    if not User.query.filter_by(username='demo').first():
        demo_user = User(
            username='demo',
            email='demo@techblog.com',
            is_admin=False
        )
        demo_user.set_password('demo123')
        db.session.add(demo_user)
        db.session.commit()
        
        # Create sample posts
        posts = [
            Post(
                title='Getting Started with Flask',
                slug='getting-started-flask',
                content='# Flask Basics\n\nFlask is a lightweight Python web framework that makes it easy to build web applications.',
                excerpt='Learn Flask basics and get started with this lightweight framework',
                category='Technology',
                author_id=demo_user.id,
                is_published=True
            ),
            Post(
                title='Database Design Best Practices',
                slug='database-design',
                content='# Database Design\n\nPrinciples of good database design including normalization, indexing, and relationships.',
                excerpt='Master the principles of effective database design',
                category='Technology',
                author_id=demo_user.id,
                is_published=True
            )
        ]
        
        for post in posts:
            db.session.add(post)
        
        db.session.commit()
        print('✓ Database seeded with sample data')
    else:
        print('✓ Demo user already exists - skipping seed')

print('✓ Database setup complete!')
print('\nYou can now login with:')
print('  Username: admin (admin account from .env)')
print('  Password: secure_password_here (from .env)')
print('\nOr demo account:')
print('  Username: demo')
print('  Password: demo123')
