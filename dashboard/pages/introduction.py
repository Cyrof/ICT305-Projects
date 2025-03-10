import dash
import plotly.express as px
from dash import dcc, html
import dash_mantine_components as dmc
from components.hoverCard import hoverableCard
from plotly.graph_objects import Figure
import dashboard.utils

dash.register_page(__name__, path="/")


def load_charts() -> dict[str, Figure]:
    return {
        "percentage_change_in_healthcare_cpi_and_income": dashboard.utils.load_chart_json(
            "percentage_change_in_healthcare_cpi_and_income.json"
        ),
        "cpi_vs_gst_line_bar": dashboard.utils.load_chart_json(
            "cpi_vs_gst_line_bar.json"
        ),
        "necessities_cpi_vs_income": dashboard.utils.load_chart_json(
            "necessities_cpi_vs_income.json"
        ),
        "cpi_bubble_map": dashboard.utils.load_chart_json("cpi_bubble_map.json"),
    }


def layout():
    charts: dict[str, Figure] = load_charts()

    return html.Div(
        [
            html.Div(
                children=[
                    # section for introduction
                    html.Section(
                        html.Article(
                            children=[
                                html.Header(
                                    # probably need to change the header to something else
                                    className="flex justify-center w-full text-3xl font-semibold",
                                    children=[
                                        html.H1(
                                            "Introduction"
                                        ),
                                    ],
                                ),
                                html.P(
                                    "Explain what we do here. List all hypothesis. Explain goal",
                                    className="border border-red-500"
                                ),
                            ]
                        ),
                    ),
                    # section for hoverable charts
                    html.Section(
                        dmc.SimpleGrid(
                            cols=4,
                            children=[
                                hoverableCard(
                                    chartID="percentage_change_in_healthcare_cpi_and_income",
                                    chart=charts["percentage_change_in_healthcare_cpi_and_income"],
                                    cardName="Healthcare",
                                    desc="Short description for healthcare",
                                    href="/healthcare"
                                ),
                                hoverableCard(
                                    chartID="cpi_vs_gst_line_bar",
                                    chart=charts["cpi_vs_gst_line_bar"],
                                    cardName="Taxes",
                                    desc="Short description for taxes",
                                    href="/taxes"
                                ),
                                hoverableCard(
                                    chartID="necessities_cpi_vs_income",
                                    chart=charts["necessities_cpi_vs_income"],
                                    cardName="Necessities",
                                    desc="Short description for necessities",
                                    href="/necessities"
                                ),
                                hoverableCard(
                                    chartID="cpi_bubble_map",
                                    chart=charts["cpi_bubble_map"],
                                    cardName="Global",
                                    desc="Short description for global",
                                    href="/global"
                                )
                            ],
                        )
                    ),
                    # conclusion
                    html.Section(
                        html.Article(
                            children=[
                                html.Header(
                                    # should probably change this header as well
                                    className="flex justify-center w-full text-3xl font-semibold",
                                    children=[
                                        html.H1(
                                            "Conclusion"
                                        ),
                                    ],
                                ),
                                html.P(
                                    "Explain our finding.",
                                    className="border border-blue-500"
                                )
                            ]
                        )
                    )
                ],
            ),
        ]
    )
