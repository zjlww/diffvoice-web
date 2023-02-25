from dominate.tags import *
from typing import Iterable

nav_counter = 0


def nav_spin(title: str, blocks: Iterable[html_tag], names: Iterable[str]):
    global nav_counter
    nav_counter += 1
    nav_id = f"navbar-{nav_counter:02d}"
    _nav = nav(id=nav_id, cls="navbar bg-light px-3 mb-3")
    _nav.add(a(title, cls="navbar-brand", href="#"))
    _pills = _nav.add(ul(cls="nav nav-pills"))
    for idx, name in enumerate(names):
        _li = li(cls="nav-item")
        _li.add(a(name, cls="nav-link", href=f"#{nav_id}-{idx:02d}"))
        _pills.add(_li)
    _div = div(
        data_bs_spy="scroll",
        data_bs_target=f"#{nav_id}",
        data_bs_root_margin="0px 0px -40%",
        data_bs_smooth_scroll="true",
        cls="scrollspy-example bg-light p-3 rounded-2",
        tabindex="0"
    )
    
    for idx, name in enumerate(names):
        _div.add(h4(name, id=f"{nav_id}-{idx:02d}"))
        _div.add(blocks[idx])
    return _nav, _div
