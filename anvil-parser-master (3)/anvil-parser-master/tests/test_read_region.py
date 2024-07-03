import context as _
from anvil import Region
import io
import secrets


def test_from_filename(tmp_path):
    filename = tmp_path / "region.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = Region.from_file(str(filename))

    assert region.data == contents


def test_from_filelike():
    contents = secrets.token_bytes()
    filelike = io.BytesIO(contents)
    region = Region.from_file(filelike)

    assert region.data == contents


def test_region_path(tmp_path):
    filename = tmp_path / "region.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = Region.from_file(str(filename))

    assert region.path == str(filename)


def test_region_coords_from_path(tmp_path):
    filename = tmp_path / "-3.5.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = Region.from_file(str(filename))

    assert region.coords == [-3, 5]


def test_region_unknown_coords_from_path_without_coords(tmp_path):
    filename = tmp_path / "region.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = Region.from_file(str(filename))

    assert region.coords == ['?', '?']


def test_region_unknown_coords_from_path_invalid_coords(tmp_path):
    filename = tmp_path / "3.4.5.mca"
    contents = secrets.token_bytes()

    with open(filename, 'wb') as f:
        f.write(contents)

    region = Region.from_file(str(filename))

    assert region.coords == ['?', '?']
