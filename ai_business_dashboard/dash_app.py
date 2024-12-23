from dash import Dash, dcc, html
import plotly.express as px

def customize_plot(fig, y_label):
    fig.update_layout(
        paper_bgcolor="#FFD1DC",  # Light pink for paper background
        plot_bgcolor="#FFFACD",  # Light yellow for plot background
        font=dict(color="#333333", family="Arial"),
        title=dict(
            text=fig.layout.title.text,
            font=dict(size=18, color="#333333"),
            x=0.5,  # Center-align title
            xanchor="center",
        ),
        xaxis=dict(
            title=dict(text="Date", font=dict(size=14, color="#333333")),
            gridcolor="#FFE4E1",  # Light pink gridlines
        ),
        yaxis=dict(
            title=dict(text=y_label, font=dict(size=14, color="#333333")),
            gridcolor="#FFE4E1", 
        ),
        legend=dict(
            orientation="h",  
            x=0.5,  
            xanchor="center",
            y=-0.2,  
        ),
    )
    return fig

def create_dash_app(combined_df):
    app = Dash(__name__)
    app.title = "Supermarket Sales Analyzer"

    # Create customized plots
    fig_revenue = px.line(
        combined_df,
        x='Date',
        y=['Revenue (Actual)', 'Revenue (Forecast)'],
        title="Revenue Trends with Predictions",
    )
    fig_revenue = customize_plot(fig_revenue, "Revenue")

    fig_profit_margins = px.line(
        combined_df,
        x='Date',
        y=['Profit Margins (Actual)', 'Profit Margins (Forecast)'],
        title="Profit Margins Trends with Predictions",
    )
    fig_profit_margins = customize_plot(fig_profit_margins, "Profit Margins")

    fig_units_sold = px.line(
        combined_df,
        x='Date',
        y=['Units Sold (Actual)', 'Units Sold (Forecast)'],
        title="Units Sold Trends with Predictions",
    )
    fig_units_sold = customize_plot(fig_units_sold, "Units Sold")

    # layout
    app.layout = html.Div(
        style={
            "backgroundColor": "#FFD1DC",
            "padding": "20px",
            "minHeight": "100vh",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
        },
        children=[
            # Title
            html.Div(
                style={
                    "backgroundColor": "#FF69B4",
                    "padding": "20px",
                    "borderRadius": "10px",
                    "textAlign": "center",
                    "marginBottom": "20px",
                    "width": "100%",
                    "maxWidth": "800px",
                },
                children=[
                    html.H1(
                        "Supermarket Sales Analyzer",
                        style={"color": "black", "margin": "0", "fontSize": "36px"},
                    )
                ],
            ),

            # Graphs
            html.Div(
                className="graph-container",
                style={"width": "100%", "maxWidth": "800px"},
                children=[dcc.Graph(figure=fig_revenue)],
            ),
            html.Div(
                className="graph-container",
                style={"width": "100%", "maxWidth": "800px"},
                children=[dcc.Graph(figure=fig_profit_margins)],
            ),
            html.Div(
                className="graph-container",
                style={"width": "100%", "maxWidth": "800px"},
                children=[dcc.Graph(figure=fig_units_sold)],
            ),

            # Single-line Textbox for Dataset Link
            html.Div(
                style={
                    "backgroundColor": "#FFFACD",
                    "padding": "5px",
                    "marginTop": "20px",
                    "borderRadius": "5px",
                    "width": "100%",
                    "maxWidth": "800px",
                    "textAlign": "left",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                },
                children=[
                    html.P(
                        [
                            "Project By: Yumna Khan @ UTDallas        |         Dataset Used: ",
                            html.A(
                                "Market Sales Data on Kaggle",
                                href="https://www.kaggle.com/datasets/willianoliveiragibin/market-sales-data?resource=download",
                                target="_blank",
                                style={
                                    "color": "#333333",
                                    "textDecoration": "underline",
                                    "fontSize": "14px",
                                },
                            ),
                        ],
                        style={"margin": "0", "fontSize": "14px"},
                    ),
                ],
            ),
        ],
    )

    return app
