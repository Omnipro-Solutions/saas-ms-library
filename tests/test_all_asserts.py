import unittest


class AllAssertsTests(unittest.TestCase):

    def test_assertEqual(self):
        self.assertEqual(1, 1)

    def test_assertNotEqual(self):
        self.assertNotEqual(1, 0)

    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertFalse(self):
        self.assertFalse(False)

    def test_assertIs(self):
        self.assertIs(True, True)

    def test_assertIsNot(self):
        self.assertIsNot(True, False)

    def test_assertIsNone(self):
        self.assertIsNone(None)

    def test_assertIsNotNone(self):
        self.assertIsNotNone(True)

    def test_assertIn(self):
        self.assertIn(1, [1, 2, 3])

    def test_assertNotIn(self):
        self.assertNotIn(4, [1, 2, 3])

    def test_assertIsInstance(self):
        self.assertIsInstance(1, int)

    def test_assertNotIsInstance(self):
        self.assertNotIsInstance(1, str)

    def test_assertGreater(self):
        self.assertGreater(2, 1)

    def test_assertGreaterEqual(self):
        self.assertGreaterEqual(2, 1)
        self.assertGreaterEqual(2, 2)

    def test_assertLess(self):
        self.assertLess(1, 2)

    def test_assertLessEqual(self):
        self.assertLessEqual(1, 2)
        self.assertLessEqual(1, 1)

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(1.1, 1.0, places=0)

    def test_assertNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 1.0, places=1)

    def test_assertRegex(self):
        self.assertRegex("abc", r"abc")

    def test_assertNotRegex(self):
        self.assertNotRegex("abc", r"def")

    def test_assertCountEqual(self):
        self.assertCountEqual([1, 2, 3], [3, 2, 1])

    def test_assertMultiLineEqual(self):
        self.assertMultiLineEqual("abc\n", "abc\n")

    def test_assertSequenceEqual(self):
        self.assertSequenceEqual([1, 2, 3], [1, 2, 3])

    def test_assertListEqual(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_assertTupleEqual(self):
        self.assertTupleEqual((1, 2, 3), (1, 2, 3))

    def test_assertSetEqual(self):
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})

    def test_assertDictEqual(self):
        self.assertDictEqual({"a": 1, "b": 2}, {"b": 2, "a": 1})

    def test_assertDictContainsSubset(self):
        self.assertDictContainsSubset({"a": 1}, {"a": 1, "b": 2})

    def test_assertRaises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_assertRaisesRegex(self):
        with self.assertRaisesRegex(ZeroDivisionError, "division by zero"):
            1 / 0

    def test_assertWarns(self):
        import warnings

        with self.assertWarns(DeprecationWarning):
            warnings.warn("deprecated", DeprecationWarning)

    def test_assertWarnsRegex(self):
        import warnings

        with self.assertWarnsRegex(DeprecationWarning, "deprecated"):
            warnings.warn("deprecated", DeprecationWarning)

    def test_assertLogs(self):
        import logging

        with self.assertLogs("logger", logging.INFO):
            logging.getLogger("logger").info("info")

    def test_assertLogsRegex(self):
        import logging

        with self.assertLogs("logger", logging.INFO) as cm:
            logging.getLogger("logger").info("info")
            self.assertRegex(cm.output[0], r"info")

    def test_skip(self):
        self.skipTest("skip")

    @unittest.skip("skip")
    def test_server(self):
        self.assertEqual(1, 2)

    @unittest.skipIf(True, "skip")
    def test_server(self):
        self.assertEqual(1, 2)

    @unittest.skipUnless(False, "skip")
    def test_server(self):
        self.assertEqual(1, 2)

    @unittest.expectedFailure
    def test_server(self):
        self.assertEqual(1, 2)
