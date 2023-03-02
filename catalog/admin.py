from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# The Modles all go here.
class AuthorBooksInLine(admin.TabularInline):
    model = Book

    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name','last_name', ('date_of_birth', 'date_of_death')]

    # exclude = ['first_name'] # Don't leave the excluded in the included.

    inlines = [AuthorBooksInLine]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance

    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')

    inlines = [BooksInstanceInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass