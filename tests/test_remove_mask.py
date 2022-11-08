from ..src.remove_mask import remove_mask


def test_remove_mask():
    assert remove_mask("125.138219-12") == "12513821912"
    assert remove_mask("120.111.210-20") == "12011121020"
    assert remove_mask("10520453913") == "10520453913"

    assert len(remove_mask("10520453913")) == len("10520453913")
    assert len(remove_mask("120.111.210-20")) == len("12011121020")
