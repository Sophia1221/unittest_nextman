import unittest
import subprocess


class TestService(unittest.TestCase):
    def test0_service_alias_create(self):
        print(20 * "*" + "TEST SERVICE creating a new user" + 20 * "*")
        service_newuser = str(subprocess.check_output(["nextman","service","alias","create","--mails","test.1@yang.de","--yes","test.unit1"]))
        print(service_newuser)
        self.assertIn("True",service_newuser)

    def test1_service_alias_add(self):
        print(20 * "*" + "TEST SERVICE add new email " + 20 * "*")
        service_addemail = str(subprocess.check_output(["nextman","service","alias","add","--mails","unittest.1@test.de","test.unit1","--yes"]))
        print(service_addemail)
        self.assertIn("True",service_addemail)

    def test2_service_alias_member(self):
        print(20 * "*" + "TEST SERVICE members check " + 20 * "*")
        servive_member = str(subprocess.check_output(["nextman", "service", "alias","members","test.unit1"]))
        print(servive_member)
        self.assertIn("unittest.1", servive_member)

    def test3_service_alias_remove(self):
        print(20 * "*" + "TEST SERVICE remove email " + 20 * "*")
        service_removemail = str(subprocess.check_output(["nextman","service","alias","remove","--yes","test.unit1","unittest.1@test.de"]))
        print(service_removemail)
        self.assertIn("True", service_removemail)

    def test4_service_alias_list(self):
        print(20 * "*" + "TEST SERVICE List all aliases " + 20 * "*")
        service_list = str(subprocess.check_output(["nextman", "service", "alias","list"]))
        print(service_list)
        self.assertIn("test.unit1", service_list)

    def test5_service_alias_delete(self):
        print(20 * "*" + "TEST SERVICE delete member" + 20 * "*")
        service_delete =str(subprocess.check_output(["nextman", "service", "alias","delete","--yes","test.unit1"]))
        print(service_delete)
        self.assertIn("True", service_delete)

    def test6_service_alias_memberall(self):
        print(20 * "*" + "TEST SERVICE all members info" + 20 * "*")
        service_member = str(subprocess.check_output(["nextman", "service", "alias", "members_all"]))
        print(service_member)
        self.assertNotIn("test.unit1",service_member)

    def test7_service_vps_list(self):
        print(20 * "*" + "TEST SERVICE list all vps" + 20 * "*")
        service_vpslist = str(subprocess.check_output(["nextman", "service", "vps", "list"]))
        print(service_vpslist)

    def test8_service_vps_info(self):
        print(20 * "*" + "TEST SERVICE check vps info" + 20 * "*")
        service_vpsinfo = str(subprocess.check_output(["nextman", "service", "vps", "info", "cloud.l3s.uni-hannover.de"]))
        print(service_vpsinfo)

    def test9_servive_website_list(self):
        print(20 * "*" + "TEST SERVICE list all website" + 20 * "*")
        service_websitelist =str(subprocess.check_output(["nextman", "service", "website", "list"]))

#vps add delete and edit haven't done>
# (/home/shuwen.yang/develop/nextman) shuwen.yang@sphere:~/develop/nextman$ nextman service vps add --username unittester --location virt --type lxc --comment test --technik unittest
# {'name': 'unittest', 'computertypes_id': 5, 'users_id': -1, 'locations_id': 53, 'manufacturers_id': 56, 'comment': 'test', 'groups_id': 2}
# glpi_api.GLPIError: (ERROR_GLPI_ADD) [{'id': False, 'message': "Out of range value for column 'users_id' at row 1"}]

# mailinglist haven't done> cant get list
# nextman service mailinglist list
# TypeError: mailinglist_list() takes 0 positional arguments but 1 was given

# website add delete and edit haven't done>
# (/home/shuwen.yang/develop/nextman) shuwen.yang@sphere:~/develop/nextman$ nextman service website add --username unittester --location virt --type php --comment test --technik unitest.yang.de
# {'name': 'unitest.yang.de', 'computertypes_id': 6, 'users_id': -1, 'locations_id': 53, 'manufacturers_id': 60, 'comment': 'test', 'groups_id': 2}
# glpi_api.GLPIError: (ERROR_GLPI_ADD) [{'id': False, 'message': "Out of range value for column 'users_id' at row 1"}]

if __name__ == '__main__':
    unittest.main()
