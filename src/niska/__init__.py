# Niška — Forensic review platform.
# © 2026 Strategos Pty Ltd. All rights reserved.
# Aut Viam Inveniam Aut Faciam

try:
    from niska_november import *  # noqa: F401, F403
    from niska_november import __version__  # noqa: F401
except ImportError:
    raise ImportError(
        "niska requires niska-november. "
        "Install with: pip install niska-november"
    )
