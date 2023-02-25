import dominate
from dominate.tags import *
from typing import List, Iterable


def header(title: str, sub: str):
    return h2(title, br(), small(sub), style="text-align: center")


def authors_row(names: Iterable[str], emails: Iterable[str]):
    rows = div(cls="row")
    for name, email in zip(names, emails):
        rows.add(div(
            [
                strong(name, style="text-align:center"),
                br(),
                a(email, href=f"mailto:{email}")
            ],
            cls="col-md-4", style="text-align: center;"
        ))
    return rows
