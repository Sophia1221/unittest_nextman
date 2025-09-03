import unittest
import subprocess
import time

class TestGroup(unittest.TestCase):
    def test0_group_create(self):
        print(20 * "*" + "TEST GROUP creating a new group with alias" + 20 * "*")
        group_new = str(subprocess.check_output(["nextman", "group", "create", "unittestgroup", "--alias", "test1", ]))
        print(group_new)
        self.assertIn("test1", group_new)

        group_ofnames = str(subprocess.check_output(["nextman", "group", "create", "--groupofnames", "unittestgroupofnames","--alias", "test3", ]))
        print(group_ofnames)
        self.assertIn("test3",group_ofnames)
        time.sleep(0.5)


    def test1_group_adduser(self):
        print(print(20 * "*" + "TEST GROUP adding a new user" + 20 * "*"))
        group_add = str(subprocess.check_output(["nextman", "group","adduser", "unittestgroup","test2"]))
        print(group_add)
        self.assertIn("test2", group_add)

        group_ofnamesadd = str(subprocess.check_output(["nextman", "group","adduser","--groupofnames", "unittestgroupofnames","test4"]))
        print(group_ofnamesadd)
        self.assertIn("test4",group_ofnamesadd)


    def test2_group_deluser_and_info(self):
        print(20 * "*" + "TEST GROUP delete user" + 20 * "*")
        group_del = subprocess.check_output(["nextman", "group", "deluser", "--alias", "unittestgroup", "test1"])
        print(group_del)
        group_info = str(subprocess.check_output(["nextman", "group", "info", "unittestgroup"]))
        self.assertNotIn("test1", group_info)

        group_ofmamesdel = subprocess.check_output(["nextman", "group", "deluser", "--groupofnames", "unittestgroupofnames", "test4"])
        print(group_ofmamesdel)
        group_ofnamesinfo = str(subprocess.check_output(["nextman", "group", "info", "--groupofnames", "unittestgroupofnames"]))
        self.assertNotIn("test4", group_ofnamesinfo)




    def test3_group_delete_andlist(self):
        print(20 * "*" + "TEST GROUP delete group" + 20 * "*")
        subprocess.check_output(["nextman", "group", "delete", "unittestgroup"])
        group_list = str(subprocess.check_output(["nextman", "group", "list"]))
        self.assertNotIn("unittestgroup", group_list)

        subprocess.check_output(["nextman", "group", "delete", "--groupofnames", "unittestgroupofnames"])
        group_listofnames = str(subprocess.check_output(["nextman", "group", "list", "--groupofnames"]))
        self.assertNotIn("unittestgroupofnames",group_listofnames)





if __name__ == '__main__':
    unittest.main()
