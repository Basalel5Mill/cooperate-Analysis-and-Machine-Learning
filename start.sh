#!/bin/bash

# Railway start script
export PORT=${PORT:-8501}
export PYTHONPATH=${PYTHONPATH:-/app}

echo "Starting Streamlit app on port $PORT..."
streamlit run app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false