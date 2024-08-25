
# ADPyBlog
## Description
Welcome to the Blog Website project! This is a dynamic blog platform developed using Django, with a sleek and modern design achieved through Tailwind CSS. The project includes a powerful text editor, TinyMCE, to facilitate an easy and rich content creation experience for bloggers.

## Features

- **Django Framework**: Utilizes Django for robust backend development and management of the blog content.
- **Tailwind CSS**: Provides a responsive and visually appealing design with utility-first CSS styling.
- **TinyMCE Editor**: Integrates TinyMCE for a user-friendly WYSIWYG (What You See Is What You Get) text editor, making blog writing and formatting straightforward.
## Setup Instructions
### Prerequisites

- Python 3.8 or higher
- Django 4.0 or higher
- Node.js and npm (for Tailwind CSS and frontend dependencies)nnel account (for localhost development)
- Tiny MEC free account.

### Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/dharayush7/adKart.git
cd adpyblog
```

#### 2. **Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3. **Install Dependencies:**
 ```bash
   pip install -r requirements.txt
```

#### 4. **Apply Migrations:**

   ```bash
   cd adPyBlog
   python manage.py migrate
   ```

#### 5. **Set Environment Variable:**

create a .env file in root lavel where manage.py exist.

```bash
TINYMEC= //api key
```

#### 6. **npm dependencies install**

```bash
cd theme/static_src
npm i
```
#### 7. **Run Tailwind Server**:
navigate the directory where manage.py exist.

- Start development server
```bash
python manage.py tailwind start
```
- Build Tailwind
```bash
python manage.py tailwind build
```


#### 8. **Run the Development Server:**

   Start the server locally:

```bash
python manage.py runserver
```










## Usage

- **Creating a Blog Post**: Go to /blog/add.
- **Viewing Blog Posts**: Visit the blog's public URL to view and interact with the published posts.
## Troubleshooting


- **Database Issues:** Ensure migrations have been applied and default data is loaded.

## 🔗 Links
[portfolio](https://www.ayushdhar.com/)



## License

[MIT]

