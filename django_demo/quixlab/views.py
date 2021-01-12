from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'quixlab/index.html')


def app_calender(request):
    return render(request, 'quixlab/app-calender.html')


def app_profile(request):
    return render(request, 'quixlab/app-profile.html')


def blank(request):
    return render(request, 'quixlab/blank.html')


def chart_chartist(request):
    return render(request, 'quixlab/chart-chartist.html')


def chart_chartjs(request):
    return render(request, 'quixlab/chart-chartjs.html')


def chart_flot(request):
    return render(request, 'quixlab/chart-flot.html')


def chart_morris(request):
    return render(request, 'quixlab/chart-morris.html')


def chart_peity(request):
    return render(request, 'quixlab/chart-peity.html')


def chart_sparkline(request):
    return render(request, 'quixlab/chart-sparkline.html')


def email_compose(request):
    return render(request, 'quixlab/email-compose.html')


def email_inbox(request):
    return render(request, 'quixlab/email-inbox.html')


def email_read(request):
    return render(request, 'quixlab/email-read.html')


def form_basic(request):
    return render(request, 'quixlab/form-basic.html')


def form_editor(request):
    return render(request, 'quixlab/form-editor.html')


def form_picker(request):
    return render(request, 'quixlab/form-picker.html')


def form_step(request):
    return render(request, 'quixlab/form-step.html')


def form_validation(request):
    return render(request, 'quixlab/form-validation.html')


def layout_blank(request):
    return render(request, 'quixlab/layout-blank.html')


def layout_boxed(request):
    return render(request, 'quixlab/layout-boxed.html')


def layout_compact_nav(request):
    return render(request, 'quixlab/layout-compact-nav.html')


def layout_dark(request):
    return render(request, 'quixlab/layout-dark.html')


def layout_fixed_header(request):
    return render(request, 'quixlab/layout-fixed-header.html')


def layout_fixed_sidebar(request):
    return render(request, 'quixlab/layout-fixed-sidebar.html')


def layout_horizontal(request):
    return render(request, 'quixlab/layout-horizontal.html')


def layout_light(request):
    return render(request, 'quixlab/layout-light.html')


def layout_one_column(request):
    return render(request, 'quixlab/layout-one-column.html')


def layout_two_column(request):
    return render(request, 'quixlab/layout-two-column.html')


def layout_vertical(request):
    return render(request, 'quixlab/layout-vertical.html')


def layout_wide(request):
    return render(request, 'quixlab/layout-wide.html')


def page_error_400(request):
    return render(request, 'quixlab/page-error-400.html')


def page_error_403(request):
    return render(request, 'quixlab/page-error-403.html')


def page_error_404(request):
    return render(request, 'quixlab/page-error-404.html')


def page_error_500(request):
    return render(request, 'quixlab/page-error-500.html')


def page_error_503(request):
    return render(request, 'quixlab/page-error-503.html')


def page_lock(request):
    return render(request, 'quixlab/page-lock.html')


def page_login(request):
    return render(request, 'quixlab/page-login.html')


def page_register(request):
    return render(request, 'quixlab/page-register.html')


def table_basic(request):
    return render(request, 'quixlab/table-basic.html')


def table_datatable(request):
    return render(request, 'quixlab/table-datatable.html')


def uc_nestedable(request):
    return render(request, 'quixlab/uc-nestedable.html')


def uc_noui_slider(request):
    return render(request, 'quixlab/uc-noui-slider.html')


def uc_sweetalert(request):
    return render(request, 'quixlab/uc-sweetalert.html')


def uc_toastr(request):
    return render(request, 'quixlab/uc-toastr.html')


def ui_accordion(request):
    return render(request, 'quixlab/ui-accordion.html')


def ui_alert(request):
    return render(request, 'quixlab/ui-alert.html')


def ui_badge(request):
    return render(request, 'quixlab/ui-badge.html')


def ui_button_group(request):
    return render(request, 'quixlab/ui-button-group.html')


def ui_button(request):
    return render(request, 'quixlab/ui-button.html')


def ui_cards(request):
    return render(request, 'quixlab/ui-cards.html')


def ui_carousel(request):
    return render(request, 'quixlab/ui-carousel.html')


def ui_dropdown(request):
    return render(request, 'quixlab/ui-dropdown.html')


def ui_list_group(request):
    return render(request, 'quixlab/ui-list-group.html')


def ui_media_object(request):
    return render(request, 'quixlab/ui-media-object.html')


def ui_modal(request):
    return render(request, 'quixlab/ui-modal.html')


def ui_pagination(request):
    return render(request, 'quixlab/ui-pagination.html')


def ui_popover(request):
    return render(request, 'quixlab/ui-popover.html')


def ui_progressbar(request):
    return render(request, 'quixlab/ui-progressbar.html')


def ui_tab(request):
    return render(request, 'quixlab/ui-tab.html')


def ui_typography(request):
    return render(request, 'quixlab/ui-typography.html')


def widgets(request):
    return render(request, 'quixlab/widgets.html')

