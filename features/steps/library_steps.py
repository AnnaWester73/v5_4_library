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

@when('användaren lämnar tillbaka boken "{title}"')
def return_book(context, title):
    for book in context.books:
        if book["title"] == title:
            book["borrowed"] = False
            return

@when('användaren kontrollerar om boken "{title}" är utlånad')
def check_if_book_is_borrowed(context, title):
    for book in context.books:
        if book["title"] == title:
            context.borrowed_status = book["borrowed"]
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

@then('ska boken "{title}" inte vara utlånad')
def book_should_not_be_borrowed(context, title):
    for book in context.books:
        if book["title"] == title:
            assert book["borrowed"] is False, f'Book "{title}" should not be borrowed'
            return

@then('ska svaret vara att boken är utlånad')
def answer_should_be_that_book_is_borrowed(context):
    assert context.borrowed_status is True, "Book should be borrowed"


@then('ska svaret vara att boken inte är utlånad')
def answer_should_be_that_book_is_not_borrowed(context):
    assert context.borrowed_status is False, "Book should not be borrowed"