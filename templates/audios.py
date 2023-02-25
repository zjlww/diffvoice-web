from dominate.tags import *
from typing import Iterable
from math import ceil
from pathlib import Path


def title_row(titles: Iterable[str]):
    row = tr()
    with row:
        for title in titles:
            if title is not None:
                td(strong(title))
            else:
                td()
    return row


def audio_row(
    audio_files: Iterable[str], 
    type: str="audio/wav",
    control_width_px: int=120
):
    row = tr()
    with row:
        for audio_file in audio_files:
            if audio_file is not None:
                td(
                    audio(
                        source(src=audio_file, type="audio/wav"),
                        controls="",
                        style=f"width: {control_width_px:d}px",
                        preload="none"
                    )
                )
            else:
                td()
    return row


def audio_table(
    audio_files: Iterable[str], 
    titles: Iterable[str]=None, 
    text: str=None,
    width: int=4,
    control_width_px: int=150
):
    # Padding Nones to ensure multiples of width:
    n_rows = ceil(len(audio_files) / width)
    n_elems = n_rows * width
    audio_files += [None] * (n_elems - len(audio_files))
    if titles is not None:
        titles += [None] * (n_elems - len(titles))

    # Construct the table:
    _div = div(cls="table-responsive")

    _table = _div.add(table(_class="table"))

    if text is not None:
        _thead = _table.add(thead())
        with _thead:
            _t = _thead.add(tr())
            _t.add(th(
                text,
                colspan=f"{width}",
                style="text-align: left;"
            ))

    _tbody = _table.add(tbody())
    with _tbody:
        for rid in range(n_rows):
            a = rid * width
            b = rid * width + width
            if titles is not None:
                title_row(titles[a: b])
            audio_row(audio_files[a: b], control_width_px=control_width_px)
        # tr(td() for _ in range(width))
    return _table


def audio_grid(
    audio_files: Iterable[str], 
    width: int=3,
    control_width_px: int=150
):
    # Construct the container:
    with div(cls="d-flex flex-row mb-3 flex-wrap justify-content-around"):
        for audio_file in audio_files:
            with div(cls=f"p-2"):
                audio(
                    source(src=audio_file, type="audio/wav"),
                    controls="",
                    style=f"width: {control_width_px:d}px",
                    preload="none"
                )


def dense_audio_table(
    speaker_names: Iterable[str],
    system_names: Iterable[str],
    system_roots: Iterable[str],
    comp_files: Iterable[str],
    control_width_px: int = 110,
    ref_root: Path=None,
    ref_files: Iterable[str]=None
):
    with div(cls="table-responsive").add(table(cls="table table-striped")):
        with thead():
            with tr():
                th("#", scope="col")
                for spk in speaker_names:
                    th(spk, scope="col")
        with tbody():
            if ref_root is not None:
                with tr():
                    th("Reference", scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                    for ref_file in ref_files:
                        if ref_file is not None:
                            td(
                                audio(
                                    source(src=ref_root + ref_file,
                                        type="audio/wav"),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none"
                                )
                            )
                        else:
                            td()

            for sys_name, sys_root in zip(system_names, system_roots):
                with tr():
                    th(sys_name, scope="row", style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;")
                    for comp_file in comp_files:
                        if comp_file is not None:
                            td(
                                audio(
                                    source(src=sys_root + comp_file,
                                           type="audio/wav"),
                                    controls="",
                                    style=f"width: {control_width_px:d}px",
                                    preload="none"
                                )
                            )
                        else:
                            td()
