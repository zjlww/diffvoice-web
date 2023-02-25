from dominate.tags import *
from .templates.audios import dense_audio_table


system_names = [
    "Ground Truth", "DiffVoice (Prompt)", "HiFi-GAN", "Autoencoder", "DiffVoice (Encoder)", "Meta-StyleSpeech", "VITS (Xvec)", "YourTTS", "FastSp.2 (Xvec)",
]

system_roots = [
    f"/diffvoice-web/samples/zeroshot/{s}/" for s in [
        "gt", "diffvoice_prompt", "hifi_gan", "ae", "diffvoice_encoder", "metastylespeech", "vits", "yourtts", "fs2"
    ]
]




def vctk_table():
    samples = [
        ("225", "p225_007.wav", "p225_005.wav"),
        ("234", "p234_069.wav", "p234_005.wav"),
        ("238", "p238_069.wav", "p238_005.wav"),
        ("245", "p245_029.wav", "p245_005.wav"),
        ("248", "p248_033.wav", "p248_005.wav"),
        ("261", "p261_064.wav", "p261_005.wav"),
        ("294", "p294_050.wav", "p294_005.wav"),
        ("302", "p302_052.wav", "p302_005.wav"),
        ("326", "p326_205.wav", "p326_005.wav"),
        ("335", "p335_037.wav", "p335_005.wav"),
        ("347", "p347_058.wav", "p347_005.wav"),
    ]
    return dense_audio_table(
        speaker_names=[s[0] for s in samples],
        ref_root="/diffvoice-web/samples/zeroshot/ref/",
        ref_files=[s[2] for s in samples],
        system_names=system_names,
        system_roots=system_roots,
        comp_files=[s[1] for s in samples]
    )


def libritts_table():
    samples = [
        ("121",  "121_121726_000005_000001.wav",  "121_121726_000004_000003.wav"),
        ("237",  "237_126133_000002_000003.wav",  "237_126133_000004_000000.wav"),
        ("260",  "260_123286_000024_000000.wav",  "260_123286_000032_000002.wav"),
        ("908",  "908_31957_000017_000002.wav",   "908_31957_000025_000001.wav"),
        ("1089", "1089_134686_000034_000003.wav", "1089_134686_000008_000000.wav"),
        ("1188", "1188_133604_000011_000003.wav", "1188_133604_000006_000000.wav"),
        ("1284", "1284_1180_000024_000001.wav",   "1284_1180_000005_000001.wav"),
        ("1580", "1580_141083_000009_000004.wav", "1580_141083_000001_000002.wav"),
        ("1995", "1995_1826_000016_000012.wav",   "1995_1826_000018_000004.wav"),
        ("2300", "2300_131720_000021_000001.wav", "2300_131720_000012_000002.wav"),
    ]
    return dense_audio_table(
        speaker_names=[s[0] for s in samples],
        ref_root="/diffvoice-web/samples/zeroshot/ref/",
        ref_files=[s[2] for s in samples],
        system_names=system_names,
        system_roots=system_roots,
        comp_files=[s[1] for s in samples]
    )