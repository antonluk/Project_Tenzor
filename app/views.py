import calendar

from flask_appbuilder import ModelView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Contact, ContactGroup, Gender, Product, Seller


def fill_gender():
    try:
        db.session.add(Gender(name="Male"))
        db.session.add(Gender(name="Female"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    list_columns = ["name", "personal_celphone", "birthday", "contact_group.name"]

    base_order = ("name", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


def pretty_year(value):
    return str(value.year)


class ContactTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Contact)

    chart_title = "Grouped Birth contacts"
    chart_type = "AreaChart"
    label_columns = ContactModelView.label_columns
    definitions = [
        {
            "group": "month_year",
            "formatter": pretty_month_year,
            "series": [(aggregate_count, "group")],
        },
        {
            "group": "year",
            "formatter": pretty_year,
            "series": [(aggregate_count, "group")],
        },
    ]


class ProductModelView(ModelView):
    datamodel = SQLAInterface(Product)

    list_columns = ["name", "price", "category", "count"]

    base_order = ("name", "price")

    show_fieldsets = [
        ("Summary", {"fields": ["name", "price", "category", "count"]})  # id_seller
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name", "price", "category", "count"]})  # id_seller
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "price", "category", "count"]})  # id_seller
    ]


class SellerModelView(ModelView):
    datamodel = SQLAInterface(Seller)

    list_columns = [
        "name",
        "address",
        "inn",
        "ogrn"
    ]

    show_fieldsets = [
        ("Summary", {"fields": ["name", "address", "inn", "ogrn"]})
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name", "address", "inn", "ogrn"]})
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "address", "inn", "ogrn"]})
    ]


db.create_all()
fill_gender()
appbuilder.add_view(
    GroupModelView, "List Groups", icon="", category="Contacts", category_icon="",
)
appbuilder.add_view(
    ContactModelView, "List Contacts", icon="", category="Contacts"
)

# appbuilder.add_separator("Contacts")
# appbuilder.add_view(
#     ContactTimeChartView, "Contacts Birth Chart", icon="fa-dashboard", category="Contacts",
# )

# appbuilder.add_separator("Products")
appbuilder.add_view(
    ProductModelView, "Product", icon="", category="Products",
)

appbuilder.add_view(
    SellerModelView, "Seller", icon="", category="Seller",
)
