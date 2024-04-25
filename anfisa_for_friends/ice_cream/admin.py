from django.contrib import admin
from ice_cream.models import Category, Topping, Wrapper, IceCream


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'output_order'
    )
    list_editable = (
        'slug',
        'is_published',
        'output_order'
    )
    inlines = (
        IceCreamInline,
    )


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug'
    )
    list_editable = (
        'slug',
    )


@admin.register(Wrapper)
class WrapperAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.empty_value_display = 'Не задано'
