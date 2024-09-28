from sqladmin import ModelView, action

from src.models import Call, Category


class BaseAdminModel(ModelView):
    page_size = 50
    page_size_options = [25, 50, 100, 200]

    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True


class CallAdmin(BaseAdminModel, model=Call):
    name = "Call"
    name_plural = "Calls"

    column_list = [Call.name, Call.emotional_tone, Call.location, Call.audio_url]
    column_searchable_list = [Call.name]
    form_columns = [Call.name, Call.audio_url, Call.emotional_tone, Call.location, Call.categories]


class CategoryAdmin(BaseAdminModel, model=Category):
    name = "Category"
    name_plural = "Categories"

    column_list = [Category.title, Category.points]
    column_searchable_list = [Category.title]
    form_columns = [Category.title, Category.points, Category.calls]

