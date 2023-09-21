import unittest

from Task_5.main import find_files


class FindFilesCase(unittest.TestCase):
    def test_invalid_path(self):
        self.assertEqual([], find_files("randomfoldername", "jpg"))

    def test_no_files_present(self):
        self.assertEqual([], find_files(".", "cpp"))

    def test_one_file_present(self):
        fpath = "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/test/test.txt"

        self.assertEqual(
            [fpath],
            find_files(
                "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/test", "txt"
            ),
        )

    def test_many_files_present(self):
        fpaths = [
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/test/a.tex",
            "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/test/b.tex",
        ]

        self.assertEqual(
            fpaths,
            sorted(
                find_files(
                    "/Users/mishashkarubski/PycharmProjects/TestLabs/Task_5/test", "tex"
                )
            ),
        )


if __name__ == "__main__":
    unittest.main()
