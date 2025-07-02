import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Corporate Financial Analysis & ML Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clean minimalistic theme
st.markdown("""
<style>
    
    .main {
        background-color: #1a1a1a;
        padding: 20px !important;
    }
    
    .stApp {
        background-color: #1a1a1a;
        color: #f5f5f5;
        padding-top: 20px !important;
    }
    
    .stSidebar {
        background-color: #2d2d2d;
        border-radius: 12px;
        padding: 16px;
    }
    
    .stSidebar > div {
        background-color: #2d2d2d;
        border-radius: 12px;
        padding: 16px;
    }
    
    /* Professional filter section containers */
    .stMultiSelect {
        background-color: #1e1e1e !important;
        border-radius: 12px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        border: 1px solid #404040 !important;
    }
    
    .stSlider {
        background-color: #1e1e1e !important;
        border-radius: 12px !important;
        padding: 16px !important;
        margin-bottom: 20px !important;
        border: 1px solid #404040 !important;
    }
    
    /* Clean sidebar text */
    .stSidebar .stMarkdown {
        color: #f5f5f5 !important;
    }
    
    .stSidebar label {
        color: #f5f5f5 !important;
        font-weight: 400 !important;
        font-size: 14px !important;
        margin-bottom: 8px !important;
    }
    
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color: #f5f5f5 !important;
        font-weight: 400 !important;
        margin-bottom: 16px !important;
    }
    
    /* Clean multi-select styling */
    .stMultiSelect > div > div {
        background-color: #333333 !important;
        border: 1px solid #555555 !important;
        border-radius: 6px !important;
        min-height: 40px !important;
        padding: 12px !important;
    }
    
    .stMultiSelect div[data-baseweb="select"] > div {
        background-color: #333333 !important;
        color: #f5f5f5 !important;
        border: none !important;
        border-radius: 6px !important;
    }
    
    .stMultiSelect div[data-baseweb="select"] input {
        color: #f5f5f5 !important;
    }
    
    /* Selected company tags - complete black with stronger selectors */
    .stMultiSelect div[data-baseweb="tag"],
    .stMultiSelect div[data-baseweb="tag"] > span,
    div[data-baseweb="tag"],
    span[data-baseweb="tag"] {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-radius: 4px !important;
        border: 1px solid #333333 !important;
        font-weight: 400 !important;
        padding: 4px 8px !important;
        margin: 2px !important;
        font-size: 12px !important;
    }
    
    .stMultiSelect div[data-baseweb="tag"] span,
    .stMultiSelect div[data-baseweb="tag"] > span,
    div[data-baseweb="tag"] span {
        background-color: #000000 !important;
        color: #ffffff !important;
        font-weight: 400 !important;
    }
    
    .stMultiSelect div[data-baseweb="tag"] svg,
    div[data-baseweb="tag"] svg {
        fill: #ffffff !important;
        opacity: 1 !important;
        color: #ffffff !important;
    }
    
    .stMultiSelect div[data-baseweb="tag"]:hover,
    div[data-baseweb="tag"]:hover {
        background-color: #222222 !important;
    }
    
    .stMultiSelect div[data-baseweb="tag"]:hover svg,
    div[data-baseweb="tag"]:hover svg {
        fill: #ffffff !important;
        opacity: 1 !important;
    }
    
    /* Force override any other tag styling */
    [data-baseweb="tag"] {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    [data-baseweb="tag"] span {
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    [data-baseweb="tag"] svg {
        fill: #ffffff !important;
    }
    
    /* Dropdown menu */
    .stMultiSelect div[data-baseweb="popover"] > div {
        background-color: #333333 !important;
        border: 1px solid #555555 !important;
        border-radius: 6px !important;
    }
    
    .stMultiSelect div[data-baseweb="menu"] {
        background-color: #333333 !important;
    }
    
    .stMultiSelect div[role="option"] {
        background-color: #333333 !important;
        color: #f5f5f5 !important;
        padding: 8px 12px !important;
    }
    
    .stMultiSelect div[role="option"]:hover {
        background-color: #444444 !important;
        color: #ffffff !important;
    }
    
    /* Control arrows and icons */
    .stMultiSelect svg {
        fill: #cccccc !important;
    }
    
    /* Clean slider styling */
    .stSlider > div > div > div {
        background-color: #333333 !important;
        border-radius: 6px !important;
        border: 1px solid #555555 !important;
        padding: 12px !important;
    }
    
    .stSlider div[data-baseweb="slider"] {
        background-color: #333333 !important;
    }
    
    .stSlider div[data-baseweb="slider"] > div {
        background-color: #2a2a2a !important;
    }
    
    /* Simple slider track */
    .stSlider > div > div > div > div > div {
        background-color: #888888 !important;
        height: 4px !important;
        border-radius: 2px !important;
    }
    
    /* Simple slider handles */
    .stSlider div[role="slider"] {
        background-color: #cccccc !important;
        border: 2px solid #ffffff !important;
        width: 16px !important;
        height: 16px !important;
        border-radius: 50% !important;
        cursor: pointer !important;
        transition: none !important;
    }
    
    .stSlider div[role="slider"]:hover {
        background-color: #ffffff !important;
    }
    
    /* Slider labels */
    .stSlider div {
        color: #f5f5f5 !important;
    }
    
    /* Clean general styling */
    h1, h2, h3, h4, h5, h6 {
        color: #f5f5f5;
    }
    
    .stMarkdown {
        color: #f5f5f5;
    }
    
    .block-container {
        background-color: #1a1a1a;
        color: #f5f5f5;
        padding: 20px !important;
        padding-top: 30px !important;
    }
    
    /* Fix header spacing */
    .main .block-container {
        padding-top: 80px !important;
    }
    
    /* Add space above metric rows */
    div[data-testid="column"] {
        margin-top: 30px !important;
        padding-top: 20px !important;
    }
    
    /* Ensure metrics are visible */
    div[data-testid="metric-container"] {
        margin-top: 20px !important;
        margin-bottom: 20px !important;
    }
    
    /* Add space to first row of content */
    .main .block-container > div:first-child {
        margin-top: 40px !important;
    }
    
    /* Universal metric container override */
    [data-testid="metric-container"],
    div[data-testid="metric-container"],
    .stMetric,
    .css-1r6slb0,
    .css-k1vhr4,
    .css-12oz5g7,
    section[data-testid="metric-container"] {
        background-color: #2d2d2d !important;
        border: 1px solid #404040 !important;
        padding: 3rem 2rem !important;
        border-radius: 12px !important;
        color: #f5f5f5 !important;
        min-height: 200px !important;
        height: auto !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        box-sizing: border-box !important;
    }
    
    /* Override any metric container with universal selector */
    * [data-testid="metric-container"] {
        min-height: 200px !important;
        padding: 3rem 2rem !important;
    }
    
    /* Force metric values styling */
    div[data-testid="metric-container"] [data-testid="metric-value"],
    div[data-testid="metric-container"] > div,
    .stMetric > div {
        font-size: 2.5rem !important;
        font-weight: bold !important;
        line-height: 1.3 !important;
        margin: 10px 0 !important;
        padding: 10px 0 !important;
    }
    
    /* Force metric labels styling */
    div[data-testid="metric-container"] [data-testid="metric-label"],
    div[data-testid="metric-container"] label,
    .stMetric label {
        font-size: 1rem !important;
        margin: 10px 0 !important;
        padding: 5px 0 !important;
    }
    
    div[data-testid="metric-container"] > label {
        color: #cccccc;
    }
    
    .stPlotlyChart {
        background-color: #1a1a1a;
        border-radius: 12px;
    }
    
    /* Chart containers with rounded corners */
    .js-plotly-plot {
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    
    /* Column containers */
    div[data-testid="column"] > div {
        border-radius: 12px !important;
        overflow: visible !important;
    }
    
    /* Custom metric card styling */
    .metric-card {
        background-color: #2d2d2d !important;
        border: 1px solid #404040 !important;
        padding: 2rem 1.5rem !important;
        border-radius: 12px !important;
        color: #f5f5f5 !important;
        min-height: 150px !important;
        height: auto !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        box-sizing: border-box !important;
        margin: 0.5rem 0 !important;
        overflow: visible !important;
    }
    
    /* Metric card value styling */
    .metric-card .metric-value {
        font-size: 2.5rem !important;
        font-weight: bold !important;
        line-height: 1.2 !important;
        margin: 0.5rem 0 !important;
        color: #f5f5f5 !important;
        white-space: nowrap !important;
        overflow: visible !important;
    }
    
    /* Metric card label styling */
    .metric-card .metric-label {
        font-size: 1rem !important;
        margin: 0.5rem 0 !important;
        color: #cccccc !important;
        font-weight: 500 !important;
        white-space: nowrap !important;
        overflow: visible !important;
    }
    
    /* Block containers */
    .block-container > div {
        border-radius: 12px !important;
        overflow: visible !important;
    }
    
    /* Clean dataframe styling */
    .dataframe {
        background-color: #2d2d2d !important;
        color: #f5f5f5 !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    .dataframe th {
        background-color: #404040 !important;
        color: #ffffff !important;
        font-weight: 500 !important;
        padding: 12px !important;
        border-bottom: 1px solid #555555 !important;
    }
    
    .dataframe td {
        padding: 10px 12px !important;
        border-bottom: 1px solid #404040 !important;
    }
    
    .dataframe tbody tr:hover {
        background-color: #3a3a3a !important;
    }
    
    .dataframe tbody tr:nth-child(odd) {
        background-color: #2d2d2d;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the financial data"""
    try:
        df = pd.read_csv('/Users/basalel/Desktop/finacial/cooperate-Analysis and Machine Learning/Financial Statements.csv')
        # Clean column names
        df.columns = df.columns.str.strip()
        df.rename(columns={
            'Company ': 'Company',
            'Market Cap(in B USD)': 'Market_Cap',
            'Category': 'Industry',
            'Inflation Rate(in US)': 'Inflation_Rate'
        }, inplace=True)
        
        # Convert column names to snake_case for consistency
        df.columns = df.columns.str.replace(' ', '_').str.replace('/', '_')
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def create_metric_card(title, value, delta=None):
    """Create a metric card with custom styling"""
    if delta:
        delta_color = "green" if delta > 0 else "red"
        delta_symbol = "+" if delta > 0 else ""
        return f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
            <div style="color: {delta_color}; font-size: 0.8rem;">{delta_symbol}{delta:.1f}%</div>
        </div>
        """
    else:
        return f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{title}</div>
        </div>
        """

def format_currency(value):
    """Format currency values"""
    if value >= 1000:
        return f"${value/1000:.1f}B"
    else:
        return f"${value:.1f}M"

def format_number(value):
    """Format large numbers"""
    if value >= 1000000:
        return f"{value/1000000:.1f}M"
    elif value >= 1000:
        return f"{value/1000:.1f}K"
    else:
        return f"{value:.0f}"

def main():
    st.title("📊 Corporate Financial Analysis Dashboard")
    
    # Load data
    df = load_data()
    if df is None:
        st.error("Failed to load data. Please check the file path.")
        return
    
    # Sidebar filters
    st.sidebar.markdown("### Filters")
    
    # Company filter
    companies = st.sidebar.multiselect(
        "Companies",
        options=sorted(df['Company'].unique()),
        default=sorted(df['Company'].unique())[:6]
    )
    
    # Year filter
    year_range = st.sidebar.slider(
        "Years",
        min_value=int(df['Year'].min()),
        max_value=int(df['Year'].max()),
        value=(2018, int(df['Year'].max()))
    )
    
    # Industry filter
    industries = st.sidebar.multiselect(
        "Industries",
        options=sorted(df['Industry'].unique()),
        default=sorted(df['Industry'].unique())
    )
    
    # Filter data
    filtered_df = df[
        (df['Company'].isin(companies)) & 
        (df['Year'] >= year_range[0]) & 
        (df['Year'] <= year_range[1]) &
        (df['Industry'].isin(industries))
    ]
    
    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
        return
    
    # Main dashboard grid layout
    
    # Row 1: Key Metrics Cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_companies = len(filtered_df['Company'].unique())
        st.markdown(create_metric_card("Companies", total_companies), unsafe_allow_html=True)
    
    with col2:
        avg_revenue = filtered_df['Revenue'].mean() / 1000  # Convert to billions
        st.markdown(create_metric_card("Avg Revenue", format_currency(avg_revenue)), unsafe_allow_html=True)
    
    with col3:
        total_market_cap = filtered_df['Market_Cap'].sum()
        st.markdown(create_metric_card("Total Market Cap", format_currency(total_market_cap)), unsafe_allow_html=True)
    
    with col4:
        avg_employees = filtered_df['Number_of_Employees'].mean()
        st.markdown(create_metric_card("Avg Employees", format_number(avg_employees)), unsafe_allow_html=True)
    
    with col5:
        avg_eps = filtered_df['Earning_Per_Share'].mean()
        st.markdown(create_metric_card("Avg EPS", f"${avg_eps:.2f}"), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Row 2: Charts Grid
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        # Revenue by Company (Bar Chart)
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Revenue by Company")
        revenue_by_company = filtered_df.groupby('Company')['Revenue'].sum().sort_values(ascending=True)
        fig1 = px.bar(
            x=revenue_by_company.values/1000,
            y=revenue_by_company.index,
            orientation='h',
            template='plotly_dark',
            color=revenue_by_company.values,
            color_continuous_scale='Viridis'
        )
        fig1.update_layout(
            height=300,
            showlegend=False,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Revenue (Billions)",
            yaxis_title="Company"
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Market Cap Distribution (Pie Chart)
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Market Cap Distribution")
        market_cap_by_company = filtered_df.groupby('Company')['Market_Cap'].mean()
        fig2 = px.pie(
            values=market_cap_by_company.values,
            names=market_cap_by_company.index,
            template='plotly_dark'
        )
        fig2.update_layout(
            height=300,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5'
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        # ROE vs ROA Scatter
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("ROE vs ROA")
        fig3 = px.scatter(
            filtered_df,
            x='ROA',
            y='ROE',
            color='Company',
            size='Market_Cap',
            template='plotly_dark'
        )
        fig3.update_layout(
            height=300,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5'
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 3: Time Series and Performance Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue Over Time (Stacked Bar)
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Revenue Trends Over Time")
        revenue_time = filtered_df.pivot_table(
            values='Revenue', 
            index='Year', 
            columns='Company', 
            aggfunc='mean'
        ).fillna(0)
        
        fig4 = go.Figure()
        for company in revenue_time.columns:
            fig4.add_trace(go.Bar(
                name=company,
                x=revenue_time.index,
                y=revenue_time[company]/1000,
            ))
        
        fig4.update_layout(
            barmode='stack',
            height=300,
            template='plotly_dark',
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Year",
            yaxis_title="Revenue (Billions)"
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Industry Performance (Horizontal Bar)
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Performance by Industry")
        industry_metrics = filtered_df.groupby('Industry').agg({
            'Revenue': 'mean',
            'Net_Income': 'mean',
            'Market_Cap': 'mean'
        }).sort_values('Revenue', ascending=True)
        
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            name='Revenue',
            y=industry_metrics.index,
            x=industry_metrics['Revenue']/1000,
            orientation='h',
            marker_color='#00cc96'
        ))
        fig5.add_trace(go.Bar(
            name='Net Income',
            y=industry_metrics.index,
            x=industry_metrics['Net_Income']/1000,
            orientation='h',
            marker_color='#ef553b'
        ))
        
        fig5.update_layout(
            barmode='group',
            height=300,
            template='plotly_dark',
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Amount (Billions)",
            yaxis_title="Industry"
        )
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 4: Financial Ratios and Employee Analysis
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Financial Ratios Box Plot
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Financial Ratios Distribution")
        ratios_df = filtered_df[['Company', 'Current_Ratio', 'Debt_Equity_Ratio']].melt(
            id_vars=['Company'], 
            var_name='Ratio_Type', 
            value_name='Value'
        )
        fig6 = px.box(
            ratios_df,
            x='Ratio_Type',
            y='Value',
            template='plotly_dark'
        )
        fig6.update_layout(
            height=300,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5'
        )
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Employee Count by Company
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Employee Count")
        employee_data = filtered_df.groupby('Company')['Number_of_Employees'].mean().sort_values(ascending=False)
        fig7 = px.bar(
            x=employee_data.index,
            y=employee_data.values,
            template='plotly_dark',
            color=employee_data.values,
            color_continuous_scale='Blues'
        )
        fig7.update_layout(
            height=300,
            showlegend=False,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Company",
            yaxis_title="Employees"
        )
        st.plotly_chart(fig7, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        # Profit Margin Analysis
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Profit Margins")
        margin_data = filtered_df.groupby('Company')['Net_Profit_Margin'].mean().sort_values(ascending=True)
        fig8 = px.bar(
            x=margin_data.values,
            y=margin_data.index,
            orientation='h',
            template='plotly_dark',
            color=margin_data.values,
            color_continuous_scale='RdYlGn'
        )
        fig8.update_layout(
            height=300,
            showlegend=False,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Net Profit Margin (%)",
            yaxis_title="Company"
        )
        st.plotly_chart(fig8, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 5: Large Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # EPS Trend Analysis
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Earnings Per Share Trends")
        fig9 = px.line(
            filtered_df,
            x='Year',
            y='Earning_Per_Share',
            color='Company',
            template='plotly_dark',
            markers=True
        )
        fig9.update_layout(
            height=400,
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5'
        )
        st.plotly_chart(fig9, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Cash Flow Analysis
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Cash Flow Analysis")
        cash_flow_data = filtered_df.groupby('Company').agg({
            'Cash_Flow_from_Operating': 'mean',
            'Cash_Flow_from_Investing': 'mean',
            'Cash_Flow_from_Financial_Activities': 'mean'
        })
        
        fig10 = go.Figure()
        fig10.add_trace(go.Bar(
            name='Operating',
            x=cash_flow_data.index,
            y=cash_flow_data['Cash_Flow_from_Operating']/1000,
            marker_color='#00cc96'
        ))
        fig10.add_trace(go.Bar(
            name='Investing',
            x=cash_flow_data.index,
            y=cash_flow_data['Cash_Flow_from_Investing']/1000,
            marker_color='#ef553b'
        ))
        fig10.add_trace(go.Bar(
            name='Financial',
            x=cash_flow_data.index,
            y=cash_flow_data['Cash_Flow_from_Financial_Activities']/1000,
            marker_color='#ffa15a'
        ))
        
        fig10.update_layout(
            barmode='group',
            height=400,
            template='plotly_dark',
            plot_bgcolor='#2d2d2d',
            paper_bgcolor='#2d2d2d',
            font_color='#f5f5f5',
            xaxis_title="Company",
            yaxis_title="Cash Flow (Billions)"
        )
        st.plotly_chart(fig10, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Machine Learning Section
    st.markdown("---")
    st.header("🤖 Machine Learning Analysis")
    
    with st.expander("EPS Performance Prediction", expanded=False):
        try:
            # Create binary target based on EPS median
            ml_df = filtered_df.copy()
            eps_threshold = ml_df['Earning_Per_Share'].median()
            ml_df['EPS_Performance'] = (ml_df['Earning_Per_Share'] > eps_threshold).astype(int)
            
            # Select features for modeling
            feature_cols = ['Market_Cap', 'Revenue', 'Gross_Profit', 'Net_Income', 'EBITDA', 
                           'ROE', 'ROA', 'ROI', 'Current_Ratio', 'Debt_Equity_Ratio']
            
            X = ml_df[feature_cols].fillna(0)
            y = ml_df['EPS_Performance']
            
            if len(X) > 10:  # Ensure enough data for modeling
                # Feature selection using Random Forest
                rf_selector = RandomForestClassifier(n_estimators=100, random_state=42)
                selector = SelectFromModel(rf_selector)
                selector.fit(X, y)
                X_selected = selector.transform(X)
                
                # Train final model
                X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.3, random_state=42)
                final_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
                final_model.fit(X_train, y_train)
                
                accuracy = final_model.score(X_test, y_test)
                st.success(f"Model trained successfully with {accuracy:.2%} accuracy")
                
                # Feature importance
                feature_importance = final_model.feature_importances_
                selected_features = [feature_cols[i] for i in range(len(feature_cols)) if selector.get_support()[i]]
                
                if len(selected_features) > 0:
                    fig_importance = px.bar(
                        x=feature_importance,
                        y=selected_features,
                        orientation='h',
                        title='Feature Importance for EPS Prediction',
                        template='plotly_dark'
                    )
                    fig_importance.update_layout(
                        plot_bgcolor='#2d2d2d',
                        paper_bgcolor='#2d2d2d',
                        font_color='#f5f5f5'
                    )
                    st.plotly_chart(fig_importance, use_container_width=True)
                
        except Exception as e:
            st.error(f"Model training failed: {str(e)}")
    
    # Data Summary Table
    st.markdown("---")
    st.subheader("📋 Financial Data Summary")
    
    # Summary statistics
    summary_stats = filtered_df.groupby('Company').agg({
        'Revenue': 'mean',
        'Net_Income': 'mean',
        'Earning_Per_Share': 'mean',
        'Market_Cap': 'mean',
        'ROE': 'mean',
        'ROA': 'mean'
    }).round(2)
    
    # Format the dataframe for better display
    formatted_summary = summary_stats.copy()
    formatted_summary['Revenue'] = formatted_summary['Revenue'].apply(lambda x: f"${x/1000:.1f}B")
    formatted_summary['Net_Income'] = formatted_summary['Net_Income'].apply(lambda x: f"${x/1000:.1f}B")
    formatted_summary['Market_Cap'] = formatted_summary['Market_Cap'].apply(lambda x: f"${x:.1f}B")
    formatted_summary['Earning_Per_Share'] = formatted_summary['Earning_Per_Share'].apply(lambda x: f"${x:.2f}")
    formatted_summary['ROE'] = formatted_summary['ROE'].apply(lambda x: f"{x:.1f}%")
    formatted_summary['ROA'] = formatted_summary['ROA'].apply(lambda x: f"{x:.1f}%")
    
    st.dataframe(formatted_summary, use_container_width=True)

if __name__ == "__main__":
    main()