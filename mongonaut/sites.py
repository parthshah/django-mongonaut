#from django.core.paginator import Paginate

try:
    import floppyforms as forms
except ImportError:
    from django import forms
    
# TODO add default widgets    

class BaseMongoAdmin(object):
    
    search_fields = []
    
    #This shows up on the DocumentListView of the Posts
    list_actions = [] 
    
    # This shows up in the DocumentDetailView of the Posts.
    document_actions = []
    
    # shows up on a particular field
    field_actions = {}
    
    fields = None
    exclude = None
    fieldsets = None
    form = forms.ModelForm
    filter_vertical = ()
    filter_horizontal = ()
    radio_fields = {}
    prepopulated_fields = {}
    formfield_overrides = {}
    readonly_fields = ()
    ordering = None

class MongoAdmin(BaseMongoAdmin):
    
    list_display = ('__str__',)
    list_display_links = ()
    list_filter = ()
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    save_as = False
    save_on_top = False
    #paginator = Paginator
    inlines = []