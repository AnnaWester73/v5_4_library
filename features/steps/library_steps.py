from behave import given, when, then


@given('att biblioteket innehåller följande böcker:')
def create_books_in_library(context):
    context.books = []

    for row in context.table:
        book = {
            "title": row["title"],
            "author": row["author"],
            "borrowed": row["borrowed"] == "yes"
        }
        context.books.append(book)


@when('användaren söker efter böcker med titel "{title}"')
def search_books_with_title(context, title):
    context.results = []

    for book in context.books:
        if book["title"] == title:
            context.results.append(book)

@when('användaren söker efter böcker av författaren "{author}"')
def search_books_by_author(context, author):
    context.results = []

    for book in context.books:
        if book["author"] == author:
            context.results.append(book)

@when('användaren lånar boken "{title}"')
def borrow_book(context, title):
    for book in context.books:
        if book["title"] == title:
            book["borrowed"] = True
            return


@then('ska följande böcker hittas:')
def books_have_been_found(context):
    expected_titles = [row["title"] for row in context.table]
    actual_titles = [book["title"] for book in context.results]

    assert expected_titles == actual_titles, f"Expected {expected_titles}, but got {actual_titles}"

@then('ska boken "{title}" vara utlånad')
def book_should_be_borrowed(context, title):
    for book in context.books:
        if book["title"] == title:
            assert book["borrowed"] is True, f'Book "{title}" should be borrowed'
            return