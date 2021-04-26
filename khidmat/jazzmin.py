JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Covid Resource & Requirements Admin | Khidmat & Zariya',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Covid Resource & Requirements Admin | Khidmat & Zariya',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    'site_logo': 'the_laundry_boys/img/logo.png',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Khidmat',

    # Copyright on the footer
    'copyright': 'NullStack Technologies',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'order.Entity',

    # Field name on user model that contains avatar image
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        # {'name': '🛒 Website',  'url': 'https://www.thelaundryboys.com'},

        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User', 'name': 'Customers'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'shop'},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
        # {'name': 'Support', 'url': 'https://nullstacks.com', 'new_window': True},
        # {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [
        'auth',
        'wagtaildocs',
        'wagtailimages',
        'taggit',
    ],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [
        'cities_light.City',
        'cities_light.Country',
        'cities_light.Region',
        'cities_light.SubRegion',
    ],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "constance", "order", "payment", "customer",
        "generic", "promotions", "shop"
    ],

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',

        'payment.Payment': 'fas fa-rupee-sign',

        'promotions.PromoCode': 'fas fa-certificate',

        'authtoken.tokenproxy': 'fas fa-key',
        'authentication.Customer': 'fas fa-user-tie',

        'constance.Config': 'fas fa-cog',

        'generic.Address': 'fas fa-address-card',
        'generic.AppHomeData': 'fas fa-table',
        'generic.CarouselItem': 'fas fa-photo-video',

        'order.Order': 'fas fa-business-time',
        'order.OrderItem': 'fas fa-tshirt',

        'shop.Item': 'fas fa-tshirt',
        'shop.Vendor': 'fas fa-user-ninja',
        'shop.Rate': 'fas fa-percent',
        'shop.SlabbedRate': 'fas fa-th-large',
        'shop.SlotRate': 'fas fa-briefcase',
        'shop.Service': 'fas fa-soap',
        'shop.TimeSlot': 'fas fa-clock',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # Add a language dropdown into the admin
    # "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": True,
    "brand_colour": "navbar-light",
    "accent": "accent-info",
    "navbar": "navbar-light",
    "no_navbar_border": True,
    "sidebar": "sidebar-light-danger",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False
}
