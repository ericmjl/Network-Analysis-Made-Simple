import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium", auto_download=["html"])




@app.cell(hide_code=True)
def _(mo):
    mo.Html(f"""
    <div class="nams-hero">
    <style>
      .nams-hero{{color:#e2e8f0;margin:0;font-family:inherit}}
      .nams-hero__grid{{display:grid;gap:22px;grid-template-columns:minmax(0,1.25fr) minmax(200px,0.85fr);padding:32px 28px;border-radius:14px;background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%)}}
      @media(max-width:760px){{.nams-hero__grid{{grid-template-columns:1fr;padding:22px 16px}}}}
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(251,191,36,0.3);background:rgba(251,191,36,0.1);border-radius:999px;color:#fbbf24;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#fbbf24}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
      .nams-check{{display:flex;flex-direction:column;gap:12px;align-items:center}}
      .nams-check-item{{display:flex;align-items:center;gap:8px;color:#94a3b8;font-size:0.82rem;font-weight:600}}
      .nams-check-dot{{width:10px;height:10px;border-radius:50%;display:inline-block}}
      .nams-check-done{{width:20px;height:20px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:0.6rem}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 00 &middot; Preface</span>
        <h1>Prerequisites<br><span class="nams-em">Check</span></h1>
        <p class="lead">Before diving into networks, let's make sure your Python foundations are solid. Dictionaries, list comprehensions, and pandas &mdash; the building blocks you'll need throughout this tutorial.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 140" style="width:100%;max-width:170px;height:auto">
          <rect x="20" y="24" width="100" height="26" rx="6" fill="none" stroke="#fbbf24" stroke-width="1.5" opacity="0.5"/>
          <circle cx="33" cy="37" r="3.5" fill="#fbbf24"/>
          <path d="M 41 37 L 48 37 M 44 34 L 44 40" stroke="#fbbf24" stroke-width="1.2" opacity="0.6" stroke-linecap="round"/>
          <line x1="56" y1="37" x2="108" y2="37" stroke="#fbbf24" stroke-width="1.5" opacity="0.25" stroke-linecap="round"/>
          <circle cx="110" cy="37" r="3" fill="#22c55e"/>
          <rect x="20" y="58" width="100" height="26" rx="6" fill="none" stroke="#fbbf24" stroke-width="1.5" opacity="0.5"/>
          <circle cx="33" cy="71" r="3.5" fill="#fbbf24"/>
          <path d="M 41 71 L 48 71 M 44 68 L 44 74" stroke="#fbbf24" stroke-width="1.2" opacity="0.6" stroke-linecap="round"/>
          <line x1="56" y1="71" x2="108" y2="71" stroke="#fbbf24" stroke-width="1.5" opacity="0.25" stroke-linecap="round"/>
          <circle cx="110" cy="71" r="3" fill="#22c55e"/>
          <rect x="20" y="92" width="100" height="26" rx="6" fill="none" stroke="#fbbf24" stroke-width="1.5" opacity="0.5"/>
          <circle cx="33" cy="105" r="3.5" fill="#fbbf24"/>
          <path d="M 41 105 L 48 105 M 44 102 L 44 108" stroke="#fbbf24" stroke-width="1.2" opacity="0.6" stroke-linecap="round"/>
          <line x1="56" y1="105" x2="108" y2="105" stroke="#fbbf24" stroke-width="1.5" opacity="0.25" stroke-linecap="round"/>
          <circle cx="110" cy="105" r="3" fill="#22c55e"/>
        </svg>
      </div>
    </div>
    </div>
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    import wigglystuff

    tour = wigglystuff.CellTour(
        steps=[
        {'cell': 0, 'title': 'Prerequisites', 'description': 'Make sure your Python foundations are ready.'},
        {'cell': 2, 'title': 'Exercises', 'description': 'Warm-up exercises on dicts and list comprehensions.'},
        {'cell': 4, 'title': 'Exercise 1', 'description': 'Reason about data structures in a list comprehension.'},
        {'cell': 6, 'title': 'Exercise 2', 'description': 'Write a function to filter dictionaries by surname.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return




@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Preface

    To get maximum benefit from this book, you should know how to program in Python.
    (Hint: it's an extremely useful skill to know!)
    In particular, knowing how to:

    1. use dictionaries,
    1. write list comprehensions, and
    1. handle `pandas` DataFrames,

    will help you a ton during the tutorial.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercises

    We have a few exercises below that should help you get warmed up.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 1

    Given the following line of code:

    ```python
    [s for s in my_fav_things if s['name'] == 'raindrops on roses']
    ```

    What are plausible data structures for `s` and `my_fav_things`?
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise 2

    Given the following data:
    """)
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
    mo.md(r"""
    Write a function that takes in the `names` list of dictionaries
    and returns the dictionaries in which the `surname` value
    matches exactly some `query_surname`.
    """)
    return


@app.function
def find_persons_with_surname(persons, query_surname):
    assert isinstance(persons, list)

    results = []
    for full_name in persons:
        if query_surname == full_name["surname"]:
            results.append(full_name)

    return results




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To test your implementation, check it with the following code.
    No errors should be raised.
    """)
    return




@app.cell
def _(names):
    results = find_persons_with_surname(names, "Lee")
    assert len(results) == 1

    results = find_persons_with_surname(names, "Elmer")
    assert len(results) == 2
    return


if __name__ == "__main__":
    app.run()
