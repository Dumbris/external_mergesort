import unittest
import numpy as np
import io
from external_sort import external_merge

class TestSort(unittest.TestCase):
    """
    Our basic test class
    """
    def generate_file(self, size=(9,9)):
        file = io.StringIO()
        file_expected = io.StringIO()
        a = np.random.randint(np.iinfo(np.int32).min,high=np.iinfo(np.int32).max, size=size, dtype=np.int32)
        np.savetxt(file, a, delimiter=" ", fmt='%d')
        np.savetxt(file_expected, np.sort(a, axis=None).reshape(size), delimiter=" ", fmt='%d')
        file.seek(0)
        return file, file_expected

    def test_small(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        sizes = [(2,2),(5,5),(10,10), (13,9), (100,100)]
        for size in sizes:
            input_file, expected_file = self.generate_file(size)
            output_file = io.StringIO()
            external_merge(input_file, output_file, 2, size, 10)
            #print(output_file.getvalue())
            #print(expected_file.getvalue())
            self.assertEqual(output_file.getvalue(), expected_file.getvalue())
            output_file.close()
            input_file.close()
            expected_file.close()

    def test_small2(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        sizes = [(100,100)]
        for size in sizes:
            input_file, expected_file = self.generate_file(size)
            output_file = io.StringIO()
            external_merge(input_file, output_file, 2, size, 10)
            #print(output_file.getvalue())
            #print(expected_file.getvalue())
            self.assertEqual(output_file.getvalue(), expected_file.getvalue())
            output_file.close()
            input_file.close()
            expected_file.close()

    def test_medium(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        size = (1000,1000)
        input_file, expected_file = self.generate_file(size)
        output_file = io.StringIO()
        external_merge(input_file, output_file, 50, size, 100)
        self.assertEqual(output_file.getvalue(), expected_file.getvalue())
        output_file.close()
        input_file.close()
        expected_file.close()

if __name__ == '__main__':
    unittest.main()