"""
HTML generator for Section: Abstract.
"""

from dominate.tags import *
from .templates.audios import audio_table, audio_grid
from dominate.util import raw


def section_abstract():
    # Compare with GuidedTTS 2 Audio Samples:
    h3("Abstract")
    p(
        """
        In this work, we present DiffVoice, a novel text to speech model based on latent diffusion. We propose to first encode speech signals into a phoneme rate latent representation with a variational autoencoder enhanced by adversarial training, and then jointly model the duration and the latent representation with a diffusion model. Subjective evaluations demonstrate that our method beats the best publicly available systems in naturalness. By adopting recent generative inverse problem solving algorithms for diffusion models, DiffVoice achieves the state of the art performance in text based speech editing, and zero shot adaptation.
        """,
        br(),
        br(),
        """The following are 6 different renditions of the abstract by a DiffVoice model. Note that this model does not have any speaker input.""",
        raw("""It samples <b>DIFF</b>erent <b>VOICE</b>s from the latent space."""),
        _class="lead"
    )
    audio_grid(
        audio_files=[f"/diffvoice-web/samples/abstract/{name}.wav" for name in ["f_0", "f_1", "f_2", "m_0", "m_1", "m_2"]],
        width=3, control_width_px=300
    )