import ldap


class LdapTest(object):

    def __init__(self):
        pass

    @staticmethod
    def ldap_connect(host, port, user, password, use_ssl=False, timeout=None):
        try:
            prefix = 'ldap'
            if use_ssl is True:
                prefix = 'ldaps'
                # ask ldap to ignore certificate errors
                ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

            if timeout:
                ldap.set_option(ldap.OPT_NETWORK_TIMEOUT, timeout)

            ldap.set_option(ldap.OPT_REFERRALS, ldap.OPT_OFF)
            server = prefix + '://' + host + ':' + '%s' % port
            connection = ldap.initialize(server)
            connection.simple_bind_s(user, password)
            return connection
        except ldap.INVALID_CREDENTIALS as ei:
            return "Invalid Username or Password"
        except ldap.SERVER_DOWN as ec:
            return "Can't contact LDAP server"
        except ldap.LDAPError as e:
            return e



