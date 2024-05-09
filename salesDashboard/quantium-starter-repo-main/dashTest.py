from dashApp import app


def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#sales-header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=10)