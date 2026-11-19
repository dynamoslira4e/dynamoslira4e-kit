import tempfile
from pathlib import Path

from dynamoslira4e_kit.core import Dynamoslira4eTool


def test_plan_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        assert Dynamoslira4eTool(tmp).plan() == []


def test_category_of_known_and_unknown():
    sorter = Dynamoslira4eTool(".")
    assert sorter.category_of("a.png") == "images"
    assert sorter.category_of("a.unknown") == "other"


def test_apply_moves_files():
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp, "note.md").write_text("hi", encoding="utf-8")
        moved = Dynamoslira4eTool(tmp).apply()
        assert moved == [("note.md", "docs")]
        assert Path(tmp, "docs", "note.md").is_file()
