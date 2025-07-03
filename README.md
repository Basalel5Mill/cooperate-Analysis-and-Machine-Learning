# Corporate Financial Analysis & Machine Learning Dashboard

A Streamlit-based dashboard for analyzing corporate financial data with machine learning predictions, featuring a professional dull black and off-white theme.

## Features

- 📊 Interactive financial data visualization
- 🤖 Machine learning EPS prediction model
- 📈 Real-time financial metrics analysis
- 🎨 Professional dark theme design
- 📱 Responsive layout for all devices

## Demo
[![▶️ Watch on YouTube](https://img.youtube.com/vi/xy21fO1WTBg/hqdefault.jpg)](https://youtu.be/xy21fO1WTBg)


*Click the button above to watch the interactive dashboard demo*

## Local Development

### Prerequisites
- Python 3.11+
- pip or poetry

### Setup with Virtual Environment

1. Clone or download the project
2. Run the setup script:
   ```bash
   ./setup.sh
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
4. Run the dashboard:
   ```bash
   streamlit run app.py
   ```

### Manual Setup

1. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

The dashboard will be available at `http://localhost:8501`

## Deployment on Railway

### Option 1: Direct Deploy Button
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

### Option 2: Manual Deployment

1. Create a new Railway project
2. Connect your GitHub repository
3. Railway will automatically detect the configuration files and deploy

### Environment Variables
No additional environment variables are required for basic functionality.

## Project Structure

```
cooperate-Analysis and Machine Learning/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── pyproject.toml                 # Poetry configuration
├── Procfile                       # Process file for deployment
├── runtime.txt                    # Python version specification
├── railway.json                   # Railway deployment config
├── nixpacks.toml                  # Nixpacks build configuration
├── setup.sh                       # Environment setup script
├── .env                          # Environment variables
├── .streamlit/
│   └── config.toml               # Streamlit configuration
└── README.md                     # This file
```

## Key Components

### Dashboard Features
- **Financial Metrics**: Revenue, Net Income, EPS, ROE analysis
- **Interactive Charts**: Time series, scatter plots, box plots
- **Company Comparison**: Multi-company analysis capabilities
- **Industry Analysis**: Cross-industry performance comparison

### Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Purpose**: EPS performance prediction (above/below median)
- **Features**: Automated feature selection
- **Accuracy**: Real-time model performance metrics

### Theme Customization
- **Colors**: Dull black (#1a1a1a) background, off-white (#f5f5f5) text
- **Professional**: Designed for business presentations
- **Responsive**: Optimized for desktop and mobile viewing

## Data Source

The dashboard currently uses synthetic financial data for demonstration purposes. To use real data:

1. Replace the `load_data()` function in `app.py`
2. Connect to your financial data source (CSV, database, API)
3. Ensure data follows the expected schema

## Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Seaborn, Matplotlib
- **Machine Learning**: Scikit-learn
- **Deployment**: Railway, Nixpacks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
1. Check the documentation
2. Review existing issues
3. Create a new issue with detailed description

---

**Note**: This dashboard is designed for educational and demonstration purposes. For production use with real financial data, ensure proper data validation, security measures, and compliance with financial regulations.
