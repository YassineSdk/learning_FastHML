from fasthtml.common import * 
import fasthtml.common as fh 
from monsterui.all import * 
from fasthtml.svg import *  
from layout import header, Sidebar, section



def dashboard():
    return Main(

        header(),
        
        Div(
            Sidebar(),
            
            section(),
        cls = "grid grid-cols-[240px_1fr] min-h-screen"

        )

    )
    