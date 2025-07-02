"""
Configuration file for the Streamlit dashboard
"""
import os

# Deployment configuration
RAILWAY_STATIC_URL = os.getenv('RAILWAY_STATIC_URL', '')
PORT = int(os.getenv('PORT', 8501))

# Theme configuration
THEME_CONFIG = {
    'primaryColor': '#f5f5f5',
    'backgroundColor': '#1a1a1a',
    'secondaryBackgroundColor': '#f5f5f5',
    'textColor': '#f5f5f5'
}

# App configuration
APP_CONFIG = {
    'page_title': 'Corporate Financial Analysis & ML Dashboard',
    'page_icon': '💼',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}