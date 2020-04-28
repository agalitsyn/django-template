from django.contrib import admin

# custom_titled_filter used for filter name alteration on admin list view
# Example:
# list_filter = (
#     ('fieldname', custom_titled_filter('My Custom Title')),
#     'plain_field',
#     ...
# )
def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

# DeleteSelectedActionMixin deletes default "delete selected" action
# from admin list view
class DeleteSelectedActionMixin:
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
