from charmhelpers.core import hookenv, templating


class DdclientHelper():
    def __init__(self):
        self.charm_config = hookenv.config()
        self.ddclient_config_file = '/etc/ddclient.conf'

    def action_function(self):
        ''' An example function for calling from an action '''
        return

    def write_config(self):
        if self.charm_config['ddclient-ssl']:
            use_ssl = 'yes'
        else:
            use_ssl = 'no'
        templating.render('ddclient.conf',
                          self.ddclient_config_file,
                          context={'protocol': self.charm_config['ddclient-protocol'],
                                   'server': self.charm_config['ddclient-server'],
                                   'login': self.charm_config['ddclient-login'],
                                   'password': self.charm_config['ddclient-password'],
                                   'ssl': use_ssl,
                                   'address': self.charm_config['ddclient-address'],
                                   })
