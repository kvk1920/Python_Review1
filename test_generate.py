import unittest
import generate


class ParserTestCase(unittest.TestCase):

    def setUp(self):
        self.parser = generate.create_parser()

    def test_output(self):
        namespace = self.parser.parse_args(("--output", "a.txt"))
        self.assertEqual(namespace.output, "a.txt")

    def test_model(self):
        namespace = self.parser.parse_args(("--mode", "model.txt"))
        self.assertEqual(namespace.model, "model.txt")

    def test_length(self):
        namespace = self.parser.parse_args(("--length", "10"))
        self.assertEqual(namespace.length, 10)


if __name__ == "__main__":
    unittest.main()