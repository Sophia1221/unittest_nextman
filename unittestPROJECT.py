import subprocess
import unittest
from unittest.mock import MagicMock, patch


class TestProject(unittest.TestCase):
    def test1_project_list(self):
        print(20 * "*" + "Print project lists" + 20 * "*")
        p_list = subprocess.check_output(["nextman", "project", "list"])
        print(p_list)

    @patch("subprocess.check_output")
    def test2_project_addandinfo(self, mock_check_output):
        print(20 * "*" + "Add project" + 20 * "*")
        mock_check_output.return_value = b"{'name': 'unittest', 'real_start_date': '2023-01-01 00:00:00', 'real_end_date': '2023-03-03 00:00:00', 'users_id': 702, 'projectstates_id': 2, 'comment': None}\n[{'id': 8, 'message': 'Item successfully added: unittest'}]\n"
        p_add = subprocess.check_output(
            [
                "nextman",
                "project",
                "add",
                "unittest",
                "tester",
                "2023-01-01",
                "2023-03-03",
                "processing",
            ]
        )
        # It won't process in system because of patch decorated the function.
        p_info = subprocess.check_output(["nextman", "project", "info", "unittest"])
        self.assertEqual(p_add, mock_check_output.return_value)
        print(p_info)

    def setUp(self):
        self.setupfakeproject()

    def setupfakeproject(self):
        self.mock_project = b"{'name': 'unittest', 'real_start_date': '2023-01-01 00:00:00', 'real_end_date': '2023-03-03 00:00:00', 'users_id': 702, 'projectstates_id': 2, 'comment': None}\n[{'id': 8, 'message': 'Item successfully added: unittest'}]\n"

    @patch("subprocess.check_output")
    def test4_project_delete(self, mock_check_output):
        print(20 * "*" + "delete project" + 20 * "*")

        mock_check_output.return_value = b"[{'8': True, 'message': ''}]\n"

        p_remove = subprocess.check_output(
            ["nextman", "project", "remove", "--yes", self.mock_project.decode("utf-8")]
        )
        ##self.mock_project.decode('utf-8') is endcoded from self.mock_project['name']
        print(p_remove)
        self.assertIn(b"[{'8': True, 'message': ''}]\n", p_remove)


##still need to test update function with mock.


if __name__ == "__main__":
    unittest.main()
