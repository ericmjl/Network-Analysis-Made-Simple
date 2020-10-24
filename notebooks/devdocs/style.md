This is the style guide for writing notebooks and markdown files for the book.

Intended as a guide when there is ambiguity in how to format something.
Updated it when new decisions are made for uncertain circumstances.

## Notebooks

### Headers

Jupyter notebook headers should begin at the 2nd level.
In other words:

```markdown
## Introdction (this is correct!)
```

should be the first header, and not:

```markdown
# Introdction (this is wrong!)
```

This allows `mkdocs` to insert the "Chapter X" heading
at the top of the compiled Markdown document.

### Exercises

Exercises should be at the 3rd level of headers.

For exercises that yield a plot, allow the exercise cell to be executed.

For exercises that modify an object that is used later, allow the exercise cell to be executed.

For exercises that are implementation-oriented, and do not affect notebook state,
it is recommended that the execution be commented out to save on execution time.

For exercises that require answering a question,
wrap the answer in a triple quote string,
use the `markdown` package to parse it into HTML,
and then use IPython's HTML display facility to show the answer
in beautiful HTML.
A convenience function called `render_html` is provided.
Here's an example:

```python
from nams.functions import render_html

def bipartite_degree_centrality_denominator():
    ans = """
Some answer goes here!
Written in **Markdown**.
"""
    return render_html(ans)
```

!!! warning "Indentation is super important!"
    Left indentation on the answer string cannot be present,
    otherwise the answer will not render correctly in HTML form!

### Solutions

Exercise solutions should be placed in the corresponding `nams.solutions.<notebook_name_without_extension>`
Python submodule.

Code solutions should always be present at the bottom of the notebook.

Use the following code block to help:

```python
import inspect
from nams.solutions import {{ notebook_name }}

print(inspect({{ notebook_name }}))
```

### Execution

Notebooks should run from top-to-bottom without erroring out.

Notebooks ideally should run in under 10 seconds.
However, if a notebook needs up to 30 seconds to finish execution,
that is acceptable.
No notebook should take on the order of minutes to finish.
