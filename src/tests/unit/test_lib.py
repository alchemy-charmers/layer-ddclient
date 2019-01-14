#!/usr/bin/python3


class TestLib():
    def test_pytest(self):
        assert True

    def test_ddclient(self, ddclient):
        ''' See if the helper fixture works to load charm configs '''
        assert isinstance(ddclient.charm_config, dict)

    # Include tests for functions in lib_ddclient
