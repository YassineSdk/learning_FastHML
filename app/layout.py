from fasthtml.common import * 
import fasthtml.common as fh 
from monsterui.all import * 
from fasthtml.svg import *  




def header():
    return Header(
            H1("Financial Dashboard"),
            P("Dashboard overview"),
            cls="bg-blue-500 p-6"



        )



def Sidebar():
    return Aside(
        "Sidebar",
        cls="bg-blue-200 p-4"
            )







def section():
    return Section(
        "Main section",
        cls="bg-green-100 p-6"
    )