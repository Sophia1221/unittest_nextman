import unittest
import subprocess
import time

class TestUser(unittest.TestCase):

    def test01_user_aliases(self):
        print(20*"*"+"TEST Returns all users in 'user:aliases' format"+20*"*")
        alias = subprocess.check_output(["nextman","user","aliases"])
        print (alias)
    pass

    def test0_user_list(self):
        list = subprocess.check_output(["nextman", "user", "list"])
        print(20 * "*" + "TEST List all users" + 20 * "*")
        print(list)
    pass

    def test1_user_create_user(self):
        print(20 * "*" + "TEST creating a new user" + 20 * "*")
        LDAPuser = subprocess.check_output(["nextman","user","create_user","-fn","FirstN","-ln","LastN","-st","another","-et","administrationhiwi","-dn","other","-physical_delivery_office_name","test",])
        print(LDAPuser)
        time.sleep(1)

    pass

    def test2_user_info(self):
        print (20 * "*" + "TEST check users info" + 20 * "*")
        infouser = subprocess.check_output(["nextman", "user", "info", "firstn.lastn"])
        print(infouser)
    pass

    def test3_user_exists(self):
        print(20 * "*" + "TEST check if users exist" + 20 * "*")
        existsuser = str(subprocess.check_output(["nextman", "user", "user_exists", "firstn.lastn"]))
        print(existsuser)
        if "True" in existsuser:
            self.assertTrue(True)
        else:
            self.assertFalse(False)
        time.sleep(1)

    def test3_user_update(self):
        print(20 * "*" + "TEST to update other info like 'title', 'telephoneNumber', 'sshPublicKey'" + 20 * "*")
        updatefield = subprocess.check_output(["nextman", "user", "update_field","-f", "title", "-v", "STAR", "firstn.lastn"])
        updatefield = subprocess.check_output(["nextman", "user", "update_field","-f", "telephoneNumber", "-v", "0152222222222", "firstn.lastn"])
        updatefield = str(subprocess.check_output(["nextman", "user", "update_field", "-f", "sshPublicKey", "-v", "qwertyuiop", "firstn.lastn"]))
        time.sleep(1)
        updatedifo = str(subprocess.check_output(["nextman", "user", "info", "firstn.lastn"]))
        print (updatedifo)
        print(updatefield)
        self.assertIn('STAR', updatedifo)
        self.assertIn('0152222222222', updatedifo)
        self.assertIn('qwertyuiop', updatedifo)


    def test4_user_delete(self):
        print(20*"*"+"TEST delete"+20*"*")
        dluser =subprocess.check_output(["nextman","user","delete_user","firstn.lastn"])
        print(dluser)


    def test5_user_exists1(self):
        print(20 * "*" + "TEST check if users doesn't exist anymore (False)" + 20 * "*")
        existsuser = str(subprocess.check_output(["nextman", "user", "user_exists", "firstn.lastn"]))
        print(existsuser)
        if "False" in existsuser:
            self.assertTrue(True)
        else:
            self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()







