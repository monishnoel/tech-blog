#!/usr/bin/env python3
"""Seed the database with sample blog posts"""

from app import create_app, db
from app.models import Post, Comment

app = create_app()

with app.app_context():
    # Create sample posts
    posts = [
        Post(
            title='Welcome to the Simplified Tech Blog',
            slug='welcome-simplified-blog',
            content='# Welcome!\n\nThis is a simplified blog platform where anyone can:\n\n- Write and publish blog posts\n- Just enter your name and share your thoughts\n- No login or registration required\n- Comment on posts from other authors\n\nEnjoy blogging!',
            category='General',
            author_name='Admin'
        ),
        Post(
            title='Getting Started with Markdown',
            slug='getting-started-markdown',
            content='# Markdown Guide\n\n## Bold and Italic\n\nYou can make text **bold** or *italic* or ***both***.\n\n## Lists\n\n- Item 1\n- Item 2\n- Item 3\n\n## Code blocks\n\n```python\nprint("Hello, World!")\n```\n\n## Links\n\n[Visit OpenAI](https://openai.com)',
            category='Tutorial',
            author_name='Tech Writer'
        ),
        Post(
            title='Tips for Writing Better Blog Posts',
            slug='tips-better-blog-posts',
            content='# Writing Tips\n\n1. **Start with a clear title** - Your title should tell readers what to expect\n2. **Use headings** - Break up your text into digestible sections\n3. **Write short paragraphs** - Easier to read and understand\n4. **Include examples** - Help readers understand concepts better\n5. **Proofread** - Always review your work before publishing',
            category='Tips',
            author_name='Writing Expert'
        ),
    ]
    
    for post in posts:
        if not Post.query.filter_by(slug=post.slug).first():
            db.session.add(post)
            print(f"Added post: {post.title}")
    
    db.session.commit()
    
    # Add some sample comments
    posts_list = Post.query.all()
    if len(posts_list) > 0 and Comment.query.count() == 0:
        comment1 = Comment(
            content='Great blog! Love the simplified approach.',
            author_name='John Reader',
            post_id=posts_list[0].id
        )
        comment2 = Comment(
            content='Thanks for the markdown tips! Very helpful.',
            author_name='Jane Writer',
            post_id=posts_list[1].id
        )
        db.session.add(comment1)
        db.session.add(comment2)
        db.session.commit()
        print("Added sample comments")

print('✓ Database seeded successfully!')
