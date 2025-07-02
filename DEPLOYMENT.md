# Deployment Guide

## Quick Railway Deployment

### Method 1: One-Click Deploy
1. Push your code to GitHub repository
2. Go to [Railway](https://railway.app)
3. Click "Deploy from GitHub repo"
4. Select your repository
5. Railway will automatically detect and deploy

### Method 2: Railway CLI
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project
railway init

# Deploy
railway up
```

## Local Testing

### Using Virtual Environment
```bash
# Run setup (first time only)
./setup.sh

# Activate environment
source venv/bin/activate

# Run dashboard
streamlit run app.py
```

### Using Docker
```bash
# Build image
docker build -t financial-dashboard .

# Run container
docker run -p 8501:8501 financial-dashboard
```

## Environment Variables

For Railway deployment, set these environment variables in Railway dashboard:

| Variable | Value | Description |
|----------|-------|-------------|
| `PORT` | `8501` | Port for the application |
| `PYTHONPATH` | `/app` | Python path |

## Files Overview

### Core Application
- `app.py` - Main Streamlit application
- `app_config.py` - Configuration settings
- `requirements.txt` - Python dependencies

### Deployment Files
- `Procfile` - Process file for Heroku-style deployments
- `railway.json` - Railway-specific configuration
- `nixpacks.toml` - Nixpacks build configuration
- `Dockerfile` - Docker container configuration
- `start.sh` - Startup script for Railway
- `deploy.py` - Python deployment script

### Environment Setup
- `setup.sh` - Local environment setup
- `pyproject.toml` - Poetry configuration
- `.env` - Environment variables template
- `.streamlit/config.toml` - Streamlit theme configuration

## Troubleshooting

### Common Issues

1. **Port binding issues**
   - Ensure `PORT` environment variable is set
   - Check if port 8501 is available locally

2. **Dependency issues**
   - Run `pip install -r requirements.txt` to install dependencies
   - Check Python version compatibility (3.11 recommended)

3. **Theme not applying**
   - Verify `.streamlit/config.toml` exists
   - Clear browser cache and reload

### Railway-Specific Issues

1. **Build failures**
   - Check Railway build logs
   - Verify all files are committed to git
   - Ensure requirements.txt is complete

2. **App not starting**
   - Check Railway deployment logs
   - Verify start command in railway.json
   - Ensure PORT environment variable is configured

## Performance Optimization

### For Production Deployment
1. Enable caching in Streamlit
2. Optimize data loading functions
3. Use compressed data formats
4. Consider CDN for static assets

### Memory Management
- Monitor Railway resource usage
- Optimize pandas operations
- Use efficient data structures

## Security Considerations

### Data Protection
- Never commit sensitive data to git
- Use environment variables for secrets
- Implement proper authentication if needed

### Network Security
- CORS is disabled for Railway deployment
- XSRF protection is disabled for Railway
- Consider enabling for production use

## Support

- Railway Documentation: https://docs.railway.app
- Streamlit Documentation: https://docs.streamlit.io
- GitHub Issues: Create issues in your repository
- try free in render.com