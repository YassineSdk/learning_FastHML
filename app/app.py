from fasthtml.common import * 
import fasthtml.common as fh 
from monsterui.all import * 
from fasthtml.svg import * 
from dashboard import dashboard

hdrs=(
        Theme.blue.headers(),
        Link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
        ),
        Style("""
            body {
                font-family: 'Inter', sans-serif;
            }
        """)
    )

app , rt = fast_app(hdrs=hdrs)

@rt
def index():
    return dashboard()

serve()

