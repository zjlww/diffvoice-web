from dominate.tags import *
from dominate.util import raw
from .templates.audios import audio_table



def editing():
    audio_root = "/diffvoice-web/samples/editing/"
    p(
        """In this section, we demonstrate DiffVoice's ability to conduct text-based speech editing (including insertion, replacement, and inpainting) with state-of-the-art quality.""",
        cls="lead"
    )
    p(
        """The following audio samples are obtained from """,
        a("RetrieverTTS", href="https://ydcustc.github.io/retrieverTTS-demo/"),
        " website. We specially thank the authors of RetrieverTTS for providing their generated samples for evaluation.",
        cls="lead"
    )
    p(
        raw("""(<strong>Speech Inpainting</strong>) Ruth was glad to hear <u><em><strong>that Philip had made a push into</strong></em></u> the world, and she was sure that his talent and courage would make a way for him. She should pray for his success at any rate, and especially that the Indians, in St. Louis, would not take his scalp."""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["6.wav", "6_diffvoice.wav", "6_retriever.wav"]],
        titles=["Original", "DiffVoice", "RetrieverTTS"],
        width=3, control_width_px=250
    )

    p(
        raw("""(<strong>Speech Insertion</strong>) Is the under side of civilization any less important than the upper side <u><em><strong>of the very same civilization</strong></em></u> merely because it is deeper and more sombre?"""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["0.wav", "0_diffvoice.wav", "0_retriever.wav"]],
        titles=["Original", "DiffVoice", "RetrieverTTS"],
        width=3, control_width_px=250
    )

    p(
        raw("""(<strong>Speech Insertion</strong>) They are chiefly formed from combinations <u><em><strong>under his success</strong></em></u> of the impressions made in childhood."""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["1.wav", "1_diffvoice.wav", "1_retriever.wav"]],
        titles=["Original", "DiffVoice", "RetrieverTTS"],
        width=3, control_width_px=250
    )
    p(
        "The following samples are taken from the website of ",
        a("EditSpeech", href="https://daxintan-cuhk.github.io/EditSpeech/"),
        ". To which we have no access of the implementation. EditSpeech is trained on VCTK, instead of LibriTTS.",
        cls="lead"
    )

    p(
        raw("""(<strong>Speech Insertion</strong>) some have accepted it as a miracle <u><em><strong>never seen before</strong></em></u> without physical explanation"""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["3.wav", "3_diffvoice.wav", "3_editspeech.wav"]],
        titles=["Original", "DiffVoice", "EditSpeech"],
        width=3, control_width_px=250
    )

    p(
        raw("""(<strong>Speech Replacement</strong>) some have accepted it as <u><em><strong><del>a miracle</del> an undeniable fact</strong></em></u> without physical explanation"""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["3.wav", "4_diffvoice.wav", "4_editspeech.wav"]],
        titles=["Original", "DiffVoice", "EditSpeech"],
        width=3, control_width_px=250
    )

    p(
        raw("""(<strong>Speech Insertion</strong>) for that <u><em><strong>theoretical and realistic</strong></em></u> reason cover should not be given"""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["2.wav", "2_diffvoice.wav", "2_editspeech.wav"]],
        titles=["Original", "DiffVoice", "EditSpeech"],
        width=3, control_width_px=250
    )

    p(
        raw("""(<strong>Speech Replacement</strong>) you should always be able to <u><em><strong><del>get out in</del> focus your research on</strong></em></u> some direction"""),
        cls="lead"
    )
    audio_table(
        [audio_root + s for s in ["5.wav", "5_diffvoice.wav", "5_editspeech.wav"]],
        titles=["Original", "DiffVoice", "EditSpeech"],
        width=3, control_width_px=250
    )