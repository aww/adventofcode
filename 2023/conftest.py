def pytest_addoption(parser):
    parser.addoption('--puzzle', action='store_true', dest="puzzle",
                 default=False, help="enable puzzle decorated tests")
    parser.addoption('--longrun', action='store_true', dest="longrun",
                 default=False, help="enable longrun decorated tests")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "puzzle: mark puzzle solution tests (generally slower)"
    )
    if not config.option.puzzle:
        if len(config.option.markexpr):
            setattr(config.option, 'markexpr', config.option.markexpr + ' and not puzzle')
        else:
            setattr(config.option, 'markexpr', 'not puzzle')

    config.addinivalue_line(
        "markers", "longrun: mark particularly long running tests, likely an unoptimized puzzle solution"
    )
    if not config.option.longrun:
        if len(config.option.markexpr):
            setattr(config.option, 'markexpr', config.option.markexpr + ' and not longrun')
        else:
            setattr(config.option, 'markexpr', 'not longrun')
