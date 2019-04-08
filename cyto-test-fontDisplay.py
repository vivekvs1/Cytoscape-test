import dash
import dash_cytoscape as cyto
import dash_html_components as html

APP = dash.Dash(__name__)
SERVER = APP.server

elements = [
    # Nodes
    {"data": {"id": "FAN", "label": "FAN \n Sound Power Level"}, "classes": "FAN"},
    {"data": {"id": "DUCT", "label": "DUCT\n 240mm x 300mm x 1mm"}, "classes": "DUCT"},
    {"data": {"id": "ELBOW", "label": "ELBOW"}, "classes": "ELBOW"},
    {"data": {"id": "ERL", "label": "END REFLECTION"}, "classes": "ERL"},
    {"data": {"id": "FLEX_DUCT", "label": "FLEX DUCT"}, "classes": "FLEX_DUCT"},
    {"data": {"id": "ROOM_EFFECT", "label": "ROOM EFFECT"}, "classes": "ROOM_EFFECT"},
    {"data": {"id": "BRANCH", "label": "BRANCH"}, "classes": "BRANCH"},
    # branches
    {"data": {"source": "DUCT", "target": "BRANCH"}},
    {"data": {"source": "FAN", "target": "DUCT"}},
    {"data": {"source": "BRANCH", "target": "ELBOW"}},
    {"data": {"source": "BRANCH", "target": "ERL"}},
    {"data": {"source": "BRANCH", "target": "FLEX_DUCT"}},
    {"data": {"source": "BRANCH", "target": "ROOM_EFFECT"}},
]


# Object declaration
cytoscape_stylesheet = [
    {
        "selector": "node",
        "style": {
            "background-color": "BFD7B5",
            "label": "data(label)",
            "font-family": "Roboto Condensed",
            "font-size": "9px",
            "text-wrap": "wrap",
            "text-max-width": 100,
            "height": 50,
            "width": 100,
            "shape": "roundrectangle",
            "text-halign": "center",
            "text-valign": "center",
        },
    },
    {
        "selector": "edge",
        "style": {
            "curve-style": "haystack",
            "line-color": "grey",
            "mid-target-arrow-color": "red",
            "mid-target-arrow-shape": "triangle",
        },
    },
]


APP.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape",
            elements=elements,
            layout={
                "name": "breadthfirst",
                "roots": '[id = "FAN"]',
                "spacingFactor": 0.8,
            },
            stylesheet=cytoscape_stylesheet,
            style={"height": "600px", "width": "1000px", "background-color": "#f5f5fa"},
        )
    ]
)


if __name__ == "__main__":
    APP.run_server(debug=True)
