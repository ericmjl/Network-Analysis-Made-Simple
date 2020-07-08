import numpy as np
from markdown import Markdown
from IPython.display import HTML


def ecdf(data):
    return np.sort(data), np.arange(1, len(data) + 1) / len(data)


def render_html(ans):
    md = Markdown()
    return HTML(md.convert(ans))
