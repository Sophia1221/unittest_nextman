import unittest
import subprocess


class TestGroup(unittest.TestCase):
    def test0_backend_glpi_info(self):
        print(20 * "*" + "Print GLPI infos" + 20 * "*")
        try:
            glpi_info= subprocess.check_output(["nextman", "backend", "glpi", "info" ],stderr=subprocess.DEVNULL,universal_newlines=True)
            print("This is Print GLPI infos that will not be displayed in the terminal"+"\n")
            #print(glpi_info)     ### or print all infomation in the terminal
        except subprocess.CalledProcessError as e:
            print("no response")
            self.fail("test 0 cant get infos")


    def test1_backend_glpi_getitems(self):
        print(20 * "*" + "get GLPI all items" + 20 * "*")
        try:
            glpi_items = subprocess.check_output(["nextman", "backend", "glpi", "get_all_items","Phone"],stderr=subprocess.DEVNULL,universal_newlines=True)
            print("This are Print GLPI all items that will not be displayed in the terminal"+"\n")
        # print(glpi_items)     ### or print all glpi items in the terminal
        except subprocess.CalledProcessError as e:
            print("no response")
            self.fail("test 1 cant get items")

    def test2_backend_glpi_list_search_options(self):
        print(20 * "*" + "GLPI search options list" + 20 * "*")
        try:
            glpi_searchoptionslist = subprocess.check_output(["nextman", "backend", "glpi", "list_search_options", "Phone"],stderr=subprocess.DEVNULL,universal_newlines=True)
            print("This are Print GLPI search options list that will not be displayed in the terminal"+ "\n")
        except subprocess.CalledProcessError as e:
            print("no response")
            self.fail("test 2 cant get lists")

    def test3_backend_ladp_listusers(self):
        print(20 * "*" + " List all ldap users" + 20 * "*")
        try:
            ladp_listusers = subprocess.check_output(["nextman", "backend", "ldap", "list_users"],stderr=subprocess.DEVNULL, universal_newlines=True)
            print("This are Print ldap all users list that will not be displayed in the terminal" + "\n")
            # print(ladp_listusers)     ### or print all ladp users in the terminal
        except subprocess.CalledProcessError as e:
            print("no response")
            self.fail("test 3 cant get lists")

    def test3_backend_ladp_listgroups(self):
        print(20 * "*" + " List all ldap groups" + 20 * "*")
        try:
            ladp_listgroups = subprocess.check_output(["nextman", "backend", "ldap", "list_groups"],stderr=subprocess.DEVNULL, universal_newlines=True)
            print("This are Print ldap all groups list that will not be displayed in the terminal" + "\n")
            # print(ladp_listgroups)     ### or print all ladp users in the terminal
        except subprocess.CalledProcessError as e:
            print("no response")
            self.fail("test 4 cant get lists")

## create group with "nextman backend ldap create_group testunit"
## TypeError: 'tuple' object cannot be interpreted as an integer
## create user with "nextman backend ldap create_user unit test unittest@l3s.com"
##
#   File "/home/shuwen.yang/develop/nextman/nextman/backend/ldap/cli.py", line 89, in ldap_create_user
#     user = UserData.from_name_and_email(
#   File "/home/shuwen.yang/develop/nextman/nextman/models.py", line 155, in from_name_and_email
#     uid = username_to_uid(first_name, last_name)
# NameError: name 'username_to_uid' is not defined

if __name__ == '__main__':
    unittest.main()
