#!/usr/bin/env python3
"""
Deployment script for Railway
"""
import subprocess
import sys
import os

def install_requirements():
    """Install requirements"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def run_app():
    """Run the Streamlit app"""
    port = os.getenv('PORT', '8501')
    subprocess.run([
        "streamlit", "run", "app.py",
        "--server.port", str(port),
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        install_requirements()
    else:
        run_app()