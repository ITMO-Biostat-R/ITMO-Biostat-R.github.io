"""Version local stylesheet links so browsers fetch CSS after design updates."""
from hashlib import sha256
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
version = sha256((root / "styles.css").read_bytes()).hexdigest()[:12]
for page in (root / "docs").rglob("*.html"):
    html = page.read_text()
    updated = re.sub(
        r'(<link\b[^>]*\bhref=")(\./|(?:\.\./)*)styles\.css(?:\?[^"<>]*)?("[^>]*>)',
        lambda match: f'{match[1]}{match[2]}styles.css?v={version}{match[3]}',
        html,
    )
    if updated != html:
        page.write_text(updated)
