import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mega_tester import show_mega_tester


infoBackgroundColor = "#E8F4F8"
infoTextColor = "#37352f"
warningBackgroundColor = "#FCF3DC"
warningTextColor = "#37352f"
successBackgroundColor = "#EDF3ED"
successTextColor = "#37352f"
errorBackgroundColor = "#FDEBEC"
errorTextColor = "#37352f"
    
# pageHoverBackgroundColor = "#F0F0EF"
# pageTextColor = "rgb(95, 94, 91)"
# pageFontWeight = "500"
# pageFontSize = "14px"

# activePageBackgroundColor = "#F0F0EF"
# activePageHoverBackgroundColor = "#E8E8E8"
# activePageTextColor = "#2D2B22"

# pageHeaderFontSize = "12px"
# pageHeaderFontWeight = "500"
# pageHeaderColor = "rgb(145, 145, 142)"


# /* First page in sidebar nav */
# [data-testid="stSidebarNav"] li:first-of-type a {{
#     background-color: {activePageBackgroundColor} !important;
# }}
# [data-testid="stSidebarNav"] li:first-of-type a:hover {{
#     background-color: {activePageHoverBackgroundColor} !important;
# }}
# [data-testid="stSidebarNav"] li:first-of-type a span {{
#     color: {activePageTextColor} !important;
# }}

# /* Other pages in sidebar nav */
# [data-testid="stSidebarNav"] li a:hover {{
#     background-color: {pageHoverBackgroundColor} !important;
# }}
# [data-testid="stSidebarNav"] li a span {{
#     color: {pageTextColor} !important;
#     font-weight: {pageFontWeight} !important;
#     font-size: {pageFontSize} !important;
# }}

# /* Headers in sidebar nav */
# [data-testid="stSidebarNav"] header {{
#     font-size: {pageHeaderFontSize} !important;
#     font-weight: {pageHeaderFontWeight} !important;
#     color: {pageHeaderColor} !important;
# }}
    
css_hacks = f"""
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"]) {{
    background-color: {infoBackgroundColor} !important;
    color: {infoTextColor} !important;
}}

[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]) {{
    background-color: {warningBackgroundColor} !important;
    color: {warningTextColor} !important;
}}

[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {{
    background-color: {successBackgroundColor} !important;
    color: {successTextColor} !important;
}}

[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]) {{
    background-color: {errorBackgroundColor} !important;
    color: {errorTextColor} !important;
}}
"""
    

show_mega_tester("Notion theme", "✍️", "https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg", css_hacks)