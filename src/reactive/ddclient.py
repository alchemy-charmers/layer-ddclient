from lib_ddclient import DdclientHelper
from charmhelpers.core import hookenv, host
from charms.reactive import set_flag, when_not, when

helper = DdclientHelper()


@when_not('ddclient.configured')
@when('apt.installed.ddclient')
def configure_ddclient():
    host.service_stop('ddclient')
    if not helper.charm_config['ddclient-enable']:
        host.service('disable', 'ddclient')
    helper.write_config()
    if helper.charm_config['ddclient-enable']:
        host.service_start('ddclient')
        host.service('enable', 'ddclient')
    hookenv.status_set('active', '')
    set_flag('ddclient.configured')


@when('config.changed')
def update_config():
    configure_ddclient()
