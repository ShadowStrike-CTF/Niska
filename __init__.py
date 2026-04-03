# © 2026 Strategos. All rights reserved.
# niska — stub package. Redirects to niska-november.
# See: https://github.com/ShadowStrike-CTF/shadowstrike-suite

try:
    from niska_november import *  # noqa: F401, F403
    from niska_november import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "niska requires niska-november. "
        "Install with: pip install niska-november"
    )
