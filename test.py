from main import LdapTest
import ldap


class LdapTTest:

    @staticmethod
    def test_true_uspw(host, port, username, password, use_ssl=False, timeout=None):

        value = LdapTest.ldap_connect(host, port, username, password, use_ssl=False, timeout=5)
        if value == "Invalid Username or Password":
            assert False
        else:
            assert True

    @staticmethod
    def test_false_uspw(host, port, username, password, use_ssl=False, timeout=None):
        value = LdapTest.ldap_connect(host, port, username, password, use_ssl=False, timeout=5)
        if value == "Invalid Username or Password":
            assert True
        else:
            assert False

    @staticmethod
    def test_connection(host, port, username, password, use_ssl=False, timeout=5):
        value = LdapTest.ldap_connect(host, port, username, password, use_ssl=False, timeout=5)
        if value == "Can't contact LDAP server":
            assert True
        else:
            assert False


print(LdapTTest.test_true_uspw("10.10.36.16", 389, "YETEN\\teknik", "Pr0da1!.th", timeout=5))
print(LdapTTest.test_false_uspw("10.10.36.16", 389, "YETEN\teknik", "Pr0da1!.th", timeout=5))
# print(LdapTTest.test_connection("10.10.36.16", 389, "YETEN\\teknik", "Pr0da1!.th", timeout=5))
print(LdapTTest.test_connection("10.1.36.16", 389, "YETEN\\teknik", "Pr0da1!.th", timeout=5))
