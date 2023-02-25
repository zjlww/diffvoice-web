"""
Online supplement for ICASSP 2023 submission.
"""
import inspect
import os 
from pathlib import Path
import dominate
from dominate.tags import *
from dominate.util import raw

from .templates import header, authors_row
from .templates.audios import audio_table


if __name__ == "__main__":
    # Where to save the generated file.
    root_path = Path(inspect.getfile(inspect.currentframe())).parent
    doc = dominate.document(title=None)

    with doc.head:
        meta(charset="utf-8")
        meta(http_equiv="X-UA-Compatible", content="IE=edge")
        meta(name="viewport", content="width=device-width, initial-scale=1")
        title("DiffVoice Online Supplement")
        link(href="/diffvoice-web/statics/bootstrap-5.2.2-dist/css/bootstrap.min.css", rel="stylesheet")

    with doc:
        # Title and Metadata:
        with div(cls="container").add(div(cls="row")):
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                header(title="DiffVoice: Text-to-Speech with Latent Diffusion", sub="Online Supplement")
                br()
                authors_row(
                    ["Zhijun Liu", "Yiwei Guo", "Kai Yu"],
                    ["zhijunliu@sjtu.edu.cn", "cantabile_kwok@sjtu.edu.cn", "kai.yu@sjtu.edu.cn"]
                )

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-danger"):
                p(
                    "This page contains > 100 MiB audio files. So it might take minutes for the audio files to load, depending on your network condition.",
                    "If you are having problems with the audios playing, you can download all audio files on this page",
                    " by downlading this ",
                    a("github repository", href="https://github.com/zjlww/zjlww.github.io"),
                    ". ", 
                    br(), br(),
                    "Some of the page's functionality requires javascript. Try to open with a different up-to-date browser. ",
                    "This page is maintained by Zhijun Liu.",
                    cls="lead"
                )

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .abstract import section_abstract
                section_abstract()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .seen_libritts import libritts_table
                h3("Results for Seen Speakers in LibriTTS")
                p(
                    "20 random speakers seen during training from the train-clean-100 split of LibriTTS.",
                    cls="lead"
                )
                libritts_table()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .zeroshot import libritts_table
                h3("Zeroshot Synthesis on LibriTTS test-clean")
                p(
                    "All speakers are unseen from the test-clean split of LibriTTS.",
                    cls="lead"
                )
                libritts_table()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .zeroshot import vctk_table
                h3("Zeroshot Synthesis on VCTK")
                p(
                    "All speakers are unseen from VCTK",
                    cls="lead"
                )
                vctk_table()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .editing import editing
                h3("Speech Editing with DiffVoice")
                editing()
                
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from .guidedtts2 import section_guidedtts2_compare
                section_guidedtts2_compare()
        
    with doc.footer:
        script(src="/diffvoice-web/statics/jquery/jquery-1.12.4.min.js")
        script(src="/diffvoice-web/statics/bootstrap-5.2.2-dist/bootstrap.min.js")

    # Script for allowing only one audio to play at the same time:
    doc.children.append(script(raw("""
        $(function(){
            $("audio").on("play", function() {
                $("audio").not(this).each(function(index, audio) {
                    audio.pause();
                    audio.currentTime = 0;
                });
            });
        });
        """)
    ))

    with open(root_path / "index.html", "w") as index:
        index.write(doc.render())
