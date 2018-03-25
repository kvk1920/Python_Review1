import unittest
import train


class ParserTestCase(unittest.TestCase):

    def test_lc(self):
        parser = train.create_parser()
        namespace = parser.parse_args(("--lc", ))
        self.assertIsNotNone(namespace.lc)

    def test_input_dir(self):
        parser = train.create_parser()
        namespace = parser.parse_args(("--input-dir", "input/"))
        self.assertEqual("input/", namespace.input_dir)

    def test_model(self):
        parser = train.create_parser()
        namespace = parser.parse_args(("--mode", "model.txt"))
        self.assertEqual(namespace.model, "model.txt")


class PrepareLineTestCase(unittest.TestCase):

    def test_lc(self):
        commands = train.create_parser().parse_args(("--lc", ))
        words = train.prepare_line("I don't like unittest__oh-oh", commands)
        for word in words:
            self.assertTrue(word.islower())
            self.assertTrue(word.isalpha())

    def test_no_lc(self):
        commands = train.create_parser().parse_args(("--model", "model.txt"))
        words = train.prepare_line('I hate unittests.,,apple;', commands)
        for word in words:
            self.assertTrue(word.isalpha())


if __name__ == "__main__":
    unittest.main()
