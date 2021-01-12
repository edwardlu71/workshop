from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource

from bokeh.palettes import Category20c, Spectral6
from bokeh.transform import cumsum
from .models import Products
from numpy import pi
import pandas as pd
from bokeh.resources import CDN


def starter(request):
    plot = figure()
    plot.circle([1, 10, 35, 27], [0, 0, 0, 0], size=20, color="blue")

    script, div = components(plot)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Starter Graph'})


def second(request):
    x = [1, 2, 3, 4, 5]
    y = [6, 10, 2, -4, 10]
    title = 'My Leaning Graph'

    plot = figure(title=title,
                  x_axis_label='High and Lows',
                  y_axis_label='Learning Topics',

                  plot_width=700,
                  plot_height=700, tools="",
                  toolbar_location=None, )

    # Formatting Graph
    cr = plot.circle(x, y, size=10, color="blue", fill_color="grey", hover_fill_color="firebrick",
                     fill_alpha=0.05, hover_alpha=0.3,
                     line_color=None, hover_line_color="white")

    plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
    plot.title.text_font_size = '20pt'
    plot.line(x, y, legend='Leaning Line', line_width=4, line_color="brown", line_dash='dashed')
    plot.background_fill_color = "lightgrey"
    plot.border_fill_color = "whitesmoke"
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    # Store components
    script, div = components(plot)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Second Graph'})


def combo(request):
    # prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    # using list comprehension to create 3 other data sets
    y0 = [i ** 2 for i in x]
    y1 = [10 ** i for i in x]
    y2 = [10 ** (i ** 2) for i in x]

    # create a new plot
    p = figure(
        tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair",  # this gives us our tools
        y_axis_type="log", y_range=[0.001, 10 ** 11], title="log axis example",
        x_axis_label='sections', y_axis_label='particles'
    )

    # add some renderers
    p.line(x, x, legend="y=x")  # thin blue line
    p.circle(x, x, legend="y=x", fill_color="white", size=8)  # adds circles to y=x line
    p.line(x, y0, legend="y=x^2", line_width=3)  # thick blue line
    p.line(x, y1, legend="y=10^x", line_color="red")  # red line
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)  # adds red circles
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")  # orange dotted line

    script, div = components(p)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Combo Graph'})


def programming(request):
    lang = ['Python', 'JavaScript', 'C#', 'PHP', 'C++', 'Java']
    counts = [25, 30, 8, 22, 12, 17]

    p = figure(x_range=lang, plot_height=450, title="Programming Languages Popularity",
               toolbar_location="below", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")

    source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())

    p.vbar(x='lang', top='counts', width=.8, color='color', legend="lang", source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    p.xgrid.grid_line_color = "black"
    p.y_range.start = 0
    p.line(x=lang, y=counts, color="black", line_width=2)

    script, div = components(p)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Programming Graph'})


def multi_plot(request):
    from bokeh.models import Range1d

    # create some data
    x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
    x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
    y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
    x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
    y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]

    # select the tools we want
    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    # the red and blue graphs will share this data range
    xr1 = Range1d(start=0, end=30)
    yr1 = Range1d(start=0, end=30)

    # only the green will use this data range
    xr2 = Range1d(start=0, end=30)
    yr2 = Range1d(start=0, end=30)

    # build our figures
    p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=600, plot_height=300)
    p1.scatter(x1, y1, size=12, color="red", alpha=0.5, legend="Bread")

    p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=600, plot_height=300)
    p2.scatter(x2, y2, size=12, color="blue", alpha=0.5, legend="Milk")

    p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=600, plot_height=300)
    p3.scatter(x3, y3, size=12, color="green", alpha=0.5, legend="Tofu")

    # plots can be a single Bokeh Model, a list/tuple, or even a dictionary
    plots = {'Red': p1, 'Blue': p2, 'Green': p3}

    script, div = components(plots)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Multiple Graph'})


def products(request):
    shoes = 0
    belts = 0
    shirts = 0
    counts = []
    items = ["Shoes", "Belts", "Shirts"]
    prod = Products.objects.values()

    for i in prod:
        if "Shoes" in i.values():
            shoes += 1
        elif ("Belts" in i.values()):
            belts += 1
        elif ("Shirts" in i.values()):
            shirts += 1
    counts.extend([shoes, belts, shirts])

    plot = figure(x_range=items, plot_height=600, plot_width=600, title="Products",
                  toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset, hover, tap, crosshair")
    plot.title.text_font_size = '20pt'

    plot.xaxis.major_label_text_font_size = "14pt"
    plot.vbar(items, top=counts, width=.4, color="firebrick", legend="Product Counts")
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Products Graph', 'debug': prod})


def pie(request):
    x = {'United States': 157, 'United Kingdom': 93, 'Japan': 89, 'China': 63,
         'Germany': 44, 'India': 42, 'Italy': 40, 'Australia': 35,
         'Brazil': 32, 'France': 31, 'Taiwan': 31, 'Spain': 29}

    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'country'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20c[len(x)]

    p = figure(plot_height=600, plot_width=800, title="Pie Chart", toolbar_location=None,
               tools="hover", tooltips="@country: @value")

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="royalblue", fill_color='color', legend='country', source=data)

    script, div = components(p)

    return render(request, 'bi/bokeh-one.html', {'script': script, 'div': div, 'title': 'Bokeh Pie Graph'})




# Quixlab ...

# Create your views here.
def index(request):
    return render(request, 'bi/index.html')


def about(request):
    return render(request, 'bi/about.html')


def app_calender(request):
    return render(request, 'bi/app-calender.html')


def app_profile(request):
    return render(request, 'bi/app-profile.html')


def blank(request):
    return render(request, 'bi/blank.html')


def chart_chartist(request):
    return render(request, 'bi/chart-chartist.html')


def chart_chartjs(request):
    return render(request, 'bi/chart-chartjs.html')


def chart_flot(request):
    return render(request, 'bi/chart-flot.html')


def chart_morris(request):
    return render(request, 'bi/chart-morris.html')


def chart_peity(request):
    return render(request, 'bi/chart-peity.html')


def chart_sparkline(request):
    return render(request, 'bi/chart-sparkline.html')


def email_compose(request):
    return render(request, 'bi/email-compose.html')


def email_inbox(request):
    return render(request, 'bi/email-inbox.html')


def email_read(request):
    return render(request, 'bi/email-read.html')


def form_basic(request):
    return render(request, 'bi/form-basic.html')


def form_editor(request):
    return render(request, 'bi/form-editor.html')


def form_picker(request):
    return render(request, 'bi/form-picker.html')


def form_step(request):
    return render(request, 'bi/form-step.html')


def form_validation(request):
    return render(request, 'bi/form-validation.html')


def layout_blank(request):
    return render(request, 'bi/layout-blank.html')


def layout_boxed(request):
    return render(request, 'bi/layout-boxed.html')


def layout_compact_nav(request):
    return render(request, 'bi/layout-compact-nav.html')


def layout_dark(request):
    return render(request, 'bi/layout-dark.html')


def layout_fixed_header(request):
    return render(request, 'bi/layout-fixed-header.html')


def layout_fixed_sidebar(request):
    return render(request, 'bi/layout-fixed-sidebar.html')


def layout_horizontal(request):
    return render(request, 'bi/layout-horizontal.html')


def layout_light(request):
    return render(request, 'bi/layout-light.html')


def layout_one_column(request):
    return render(request, 'bi/layout-one-column.html')


def layout_two_column(request):
    return render(request, 'bi/layout-two-column.html')


def layout_vertical(request):
    return render(request, 'bi/layout-vertical.html')


def layout_wide(request):
    return render(request, 'bi/layout-wide.html')


def page_error_400(request):
    return render(request, 'bi/page-error-400.html')


def page_error_403(request):
    return render(request, 'bi/page-error-403.html')


def page_error_404(request):
    return render(request, 'bi/page-error-404.html')


def page_error_500(request):
    return render(request, 'bi/page-error-500.html')


def page_error_503(request):
    return render(request, 'bi/page-error-503.html')


def page_lock(request):
    return render(request, 'bi/page-lock.html')


def page_login(request):
    return render(request, 'bi/page-login.html')


def page_register(request):
    return render(request, 'bi/page-register.html')


def table_basic(request):
    return render(request, 'bi/table-basic.html')


def table_datatable(request):
    return render(request, 'bi/table-datatable.html')


def uc_nestedable(request):
    return render(request, 'bi/uc-nestedable.html')


def uc_noui_slider(request):
    return render(request, 'bi/uc-noui-slider.html')


def uc_sweetalert(request):
    return render(request, 'bi/uc-sweetalert.html')


def uc_toastr(request):
    return render(request, 'bi/uc-toastr.html')


def ui_accordion(request):
    return render(request, 'bi/ui-accordion.html')


def ui_alert(request):
    return render(request, 'bi/ui-alert.html')


def ui_badge(request):
    return render(request, 'bi/ui-badge.html')


def ui_button_group(request):
    return render(request, 'bi/ui-button-group.html')


def ui_button(request):
    return render(request, 'bi/ui-button.html')


def ui_cards(request):
    return render(request, 'bi/ui-cards.html')


def ui_carousel(request):
    return render(request, 'bi/ui-carousel.html')


def ui_dropdown(request):
    return render(request, 'bi/ui-dropdown.html')


def ui_list_group(request):
    return render(request, 'bi/ui-list-group.html')


def ui_media_object(request):
    return render(request, 'bi/ui-media-object.html')


def ui_modal(request):
    return render(request, 'bi/ui-modal.html')


def ui_pagination(request):
    return render(request, 'bi/ui-pagination.html')


def ui_popover(request):
    return render(request, 'bi/ui-popover.html')


def ui_progressbar(request):
    return render(request, 'bi/ui-progressbar.html')


def ui_tab(request):
    return render(request, 'bi/ui-tab.html')


def ui_typography(request):
    return render(request, 'bi/ui-typography.html')


def widgets(request):
    return render(request, 'bi/widgets.html')

