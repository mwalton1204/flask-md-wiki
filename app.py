import os
from flask import Flask, render_template
import markdown

app = Flask(__name__)

# Folder where markdown files are stored
app.config['CONTENT_FOLDER'] = 'content'

@app.route('/')
def home():
    """
    Home page, displaying links to available Markdown pages
    """
    
    pages = [f.replace('.md', '') for f in os.listdir(app.config['CONTENT_FOLDER']) if f.endswith('.md')]
    return render_template('index.html', pages=pages)

@app.route('/page/<slug>')
def view_page(slug):
    """
    View a specific page by its slug (slug is the markdown filename without extension).
    """
    
    md_file_path = os.path.join(app.config['CONTENT_FOLDER'], f"{slug}.md")
    
    if not os.path.exists(md_file_path):
        return "Page not found", 404
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
        
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    
    return render_template('page.html', title=slug, content=html_content)

if __name__ == '__main__':
    app.run(debug=True)