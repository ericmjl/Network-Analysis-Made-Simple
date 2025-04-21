import marimo

__generated_with = "0.12.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Preface

        To get maximum benefit from this book, you should know how to program in Python.
        (Hint: it's an extremely useful skill to know!)
        In particular, knowing how to:

        1. use dictionaries,
        1. write list comprehensions, and
        1. handle `pandas` DataFrames,

        will help you a ton during the tutorial.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Exercises

        We have a few exercises below that should help you get warmed up.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 1

        Given the following line of code:

        ```python
        [s for s in my_fav_things if s[‘name’] == ‘raindrops on roses’]
        ```

        What are plausible data structures for `s` and `my_fav_things`?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise 2

        Given the following data:
        """
    )
    return


@app.cell
def _():
    names = [
        {"name": "Eric", "surname": "Ma"},
        {"name": "Jeffrey", "surname": "Elmer"},
        {"name": "Mike", "surname": "Lee"},
        {"name": "Jennifer", "surname": "Elmer"},
    ]
    return (names,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Write a function that takes in the `names` list of dictionaries
        and returns the dictionaries in which the `surname` value
        matches exactly some `query_surname`.
        """
    )
    return


@app.cell
def _(________, __________, ___________):
    def find_persons_with_surname(persons, query_surname):
        # Assert that the persons parameter is a list.
        # This is a good defensive programming practice.
        assert isinstance(persons, list)

        results = []
        for ______ in ______:
            if ___________ == __________:
                results.append(________)

        return results

    return (find_persons_with_surname,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To test your implementation, check it with the following code.
        No errors should be raised.
        """
    )
    return


@app.cell
def _(find_persons_with_surname, names):
    # Test your result below.
    results = find_persons_with_surname(names, "Lee")
    assert len(results) == 1

    results = find_persons_with_surname(names, "Elmer")
    assert len(results) == 2
    return (results,)


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
