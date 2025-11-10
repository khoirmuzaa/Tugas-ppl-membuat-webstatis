import os

def test_index_exists():
    assert os.path.exists("index.html"), "File index.html tidak ditemukan!"

def test_nim_terdapat_dalam_file():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "230411100068" in content, "NIM tidak ditemukan di dalam index.html"