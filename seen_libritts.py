from .templates.audios import dense_audio_table


def libritts_table():
    samples = [26, 40, 226, 887, 1069, 1624, 1737, 2136, 2817, 3240, 3699, 4088, 5750, 7302, 7511, 7794, 7800, 7859, 8324, 8580]
    return dense_audio_table(
        speaker_names=[str(s) for s in samples],
        system_names=["Ground Truth", "DiffVoice",  "HiFi-GAN", "Autoencoder", "VITS", "FastSpeech 2"],
        system_roots=[f"/diffvoice-web/samples/libritts/{sys}/" for sys in [
            "gt", "diffvoice", "hifigan", "ae", "vits", "fs2"
        ]],
        comp_files=[f"{s}.wav" for s in samples],
        control_width_px=110
    )
