import test_data
from islinker import URLLinesChecker as ULC


def test_split_lines():
    new_data = ULC(test_data.line_x2)
    assert len(new_data.split_lines()) == 2


def test_process_lines_is_link():
    new_data = ULC(test_data.is_link)
    new_data.split_lines()
    assert new_data.process_lines()[0] == test_data.is_link


def test_process_lines_not_link():
    new_data = ULC(test_data.not_link)
    new_data.split_lines()
    assert not new_data.process_lines()


def test_prepare_url_spaces():
    url = ULC.prepare_url(test_data.link_for_prep)
    assert url[0] != ' '
    assert url[len(url) - 1] != ' '


def test_prepare_url_http_added():
    url = ULC.prepare_url(test_data.link_for_prep)
    assert dict(enumerate("https://")) == dict(enumerate(url[:8]))

