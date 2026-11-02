"""Refresh standalone Quarto downloads from the course sources."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
destination = root / "downloads"
destination.mkdir(exist_ok=True)
for relative in (
    "code/basic_r.qmd",
    "code/distributions_clt_ci.qmd",
    "code/stats_ttest_chi.qmd",
    "homeworks/HW_virt_hospital.qmd",
):
    source = root / relative
    text = source.read_text()
    text = text.replace(
        "\neditor: visual\n",
        "\nformat:\n  html:\n    toc: true\n    code-copy: true\neditor: visual\n",
        1,
    )
    (destination / source.name).write_text(text)
