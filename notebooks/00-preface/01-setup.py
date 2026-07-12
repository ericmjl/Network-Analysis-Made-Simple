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
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(34,211,238,0.3);background:rgba(34,211,238,0.1);border-radius:999px;color:#22d3ee;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.4rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#22d3ee}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Interactive Tutorial</span>
        <h1>Network Analysis<br><span class="nams-em">Made Simple</span></h1>
        <p class="lead">A hands-on guide to graphs, NetworkX, and the algorithms that reveal hidden structure in relational data &mdash; from protein interactions to social networks.</p>
        <div class="nams-byline">By <b>Eric Ma</b> &middot; Network Analysis Made Simple<br>Source: <b>github.com/ericmjl/Network-Analysis-Made-Simple</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 140" style="width:100%;max-width:180px;height:auto">
          <line x1="70" y1="30" x2="35" y2="55" stroke="#22d3ee" stroke-width="1.4" opacity="0.4"/>
          <line x1="70" y1="30" x2="105" y2="48" stroke="#22d3ee" stroke-width="1.4" opacity="0.4"/>
          <line x1="70" y1="30" x2="42" y2="92" stroke="#22d3ee" stroke-width="1.4" opacity="0.3"/>
          <line x1="70" y1="30" x2="88" y2="88" stroke="#22d3ee" stroke-width="1.4" opacity="0.3"/>
          <line x1="35" y1="55" x2="20" y2="25" stroke="#22d3ee" stroke-width="1.2" opacity="0.25"/>
          <line x1="35" y1="55" x2="42" y2="92" stroke="#22d3ee" stroke-width="1.2" opacity="0.25"/>
          <line x1="105" y1="48" x2="88" y2="88" stroke="#22d3ee" stroke-width="1.2" opacity="0.25"/>
          <line x1="105" y1="48" x2="118" y2="78" stroke="#22d3ee" stroke-width="1.2" opacity="0.25"/>
          <line x1="42" y1="92" x2="88" y2="88" stroke="#22d3ee" stroke-width="1" opacity="0.15"/>
          <line x1="88" y1="88" x2="118" y2="78" stroke="#22d3ee" stroke-width="1" opacity="0.15"/>
          <circle cx="70" cy="30" r="7" fill="#22d3ee"/>
          <circle cx="35" cy="55" r="5" fill="#38bdf8"/>
          <circle cx="105" cy="48" r="5" fill="#38bdf8"/>
          <circle cx="42" cy="92" r="5" fill="#38bdf8"/>
          <circle cx="88" cy="88" r="4.5" fill="#0ea5e9"/>
          <circle cx="20" cy="25" r="3.5" fill="#0ea5e9" opacity="0.8"/>
          <circle cx="118" cy="78" r="3.5" fill="#0ea5e9" opacity="0.8"/>
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
        {'cell': 0, 'title': 'Setup', 'description': 'Getting started with pixi and marimo for reproducible notebooks.'},
        {'cell': 4, 'title': 'Quick Setup', 'description': 'Three steps: clone, install pixi, run marimo.'},
        {'cell': 5, 'title': 'What this does', 'description': 'pixi handles deps, marimo handles interactivity.'},
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
    ## Introduction

    In order to get the most of this book,
    you will want to be able to execute the examples in the notebooks,
    modify them, break the code, and fix it.
    Pedagogically, that is the best way for you to learn the concepts.
    Here's the recommended way to get set up.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Quick Setup

    To get started with the notebooks, follow these simple steps:

    1. Git clone the repository: https://github.com/ericmjl/Network-Analysis-Made-Simple

    2. **Install pixi** (the package manager):
       Follow the installation instructions at [https://pixi.sh](https://pixi.sh)

    3. **Run the notebooks**:
       ```bash
       pixi run marimo edit --no-token notebooks/
       ```

    Once Marimo is launched, on the bottom, click on "on startup", "on cell change", and "on module change" to disable automatic execution. This will allow us to mimic original Jupyter behaviour, which is advantageous for a teaching setting (but toggle them back to "autorun" when you're done with the tutorial).

    That's it! Pixi ensures a clean, isolated environment for running the notebooks with all necessary dependencies automatically managed.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## What this does

    - **pixi** is a fast package manager that handles dependency resolution and environments
    - **marimo** is an interactive notebook environment optimized for Python
    - All required packages are automatically installed via the pixi manifest
    - No manual environment setup, conda environments, or Docker containers needed

    This approach ensures reproducible execution of the tutorial content.
    """)
    return


if __name__ == "__main__":
    app.run()
