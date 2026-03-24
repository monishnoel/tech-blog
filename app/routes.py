from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Post, Comment
from datetime import datetime
import re

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__, url_prefix='/api')

# --- MAIN ROUTES ---
@main_bp.route('/')
def index():
    """Home page - displays all posts"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', posts=posts)

@main_bp.route('/post/<slug>')
def view_post(slug):
    """View a single blog post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    post.increment_views()
    
    comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.created_at.desc()).all()
    
    return render_template('post.html', post=post, comments=comments)

@main_bp.route('/category/<category>')
def category(category):
    """View posts by category"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category=category).order_by(Post.created_at.desc()).paginate(page=page, per_page=10)
    
    return render_template('category.html', category=category, posts=posts)

@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')

# --- CREATE/EDIT BLOG POST ROUTES ---
@main_bp.route('/new-post', methods=['GET', 'POST'])
def new_post():
    """Create a new blog post"""
    if request.method == 'POST':
        author_name = request.form.get('author_name', '').strip()
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        category = request.form.get('category', 'General').strip()
        
        # Validation
        if not all([author_name, title, content]):
            flash('Author name, title, and content are required', 'danger')
            return redirect(url_for('main.new_post'))
        
        # Generate slug
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        
        # Check if slug already exists
        if Post.query.filter_by(slug=slug).first():
            flash('A post with this title already exists', 'danger')
            return redirect(url_for('main.new_post'))
        
        # Create post
        post = Post(
            title=title,
            slug=slug,
            content=content,
            category=category,
            author_name=author_name
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('main.view_post', slug=post.slug))
    
    return render_template('new_post.html')

@main_bp.route('/post/<slug>/edit', methods=['GET', 'POST'])
def edit_post(slug):
    """Edit a blog post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    if request.method == 'POST':
        post.author_name = request.form.get('author_name', '').strip()
        post.title = request.form.get('title', '').strip()
        post.content = request.form.get('content', '').strip()
        post.category = request.form.get('category', 'General').strip()
        post.updated_at = datetime.utcnow()
        
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('main.view_post', slug=post.slug))
    
    return render_template('edit_post.html', post=post)

@main_bp.route('/post/<slug>/delete', methods=['POST'])
def delete_post(slug):
    """Delete a blog post"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.index'))

# --- API ROUTES ---
@api_bp.route('/comment/add', methods=['POST'])
def add_comment():
    """Add a comment to a post"""
    data = request.get_json()
    post_id = data.get('post_id')
    author_name = data.get('author_name', '').strip()
    content = data.get('content', '').strip()
    
    if not all([post_id, author_name, content]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    post = Post.query.get_or_404(post_id)
    
    comment = Comment(
        content=content,
        author_name=author_name,
        post_id=post_id
    )
    
    db.session.add(comment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Comment added successfully'})

@api_bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
def delete_comment(comment_id):
    """Delete a comment"""
    comment = Comment.query.get_or_404(comment_id)
    
    db.session.delete(comment)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Comment deleted'})

@api_bp.route('/search')
def search():
    """Search blog posts"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify({'posts': []})
    
    posts = Post.query.filter(
        (Post.title.ilike(f'%{query}%')) | 
        (Post.content.ilike(f'%{query}%'))
    ).limit(10).all()
    
    return jsonify({
        'posts': [{
            'id': p.id,
            'title': p.title,
            'slug': p.slug,
            'excerpt': p.get_summary()
        } for p in posts]
    })

@api_bp.route('/stats')
def stats():
    """Get blog statistics"""
    return jsonify({
        'total_posts': Post.query.count(),
        'total_comments': Comment.query.count(),
        'total_views': sum(p.view_count for p in Post.query.all())
    })
