#!/usr/bin/python

from __future__ import with_statement
from csv_index_supplant import CsvSupplant
import unittest, os

class CsvSupplantTest(unittest.TestCase):
    def setUp(self):
        with open('tmpTestFile', 'w') as self.sourceFile:
            self.sourceFile.write('firstArg,secondArg,thirdArg')
    
    def tearDown(self):
        self.sourceFile.close()
        os.remove(self.sourceFile.name)

    def test_supplant_1_args_ok(self):
        parser = CsvSupplant(self.sourceFile.name, ',', 'TEST ({0})')
        self.assertEqual('TEST (firstArg)\n', parser.supplant())
    
    def test_supplant_2_args_ok(self):
        parser = CsvSupplant(self.sourceFile.name, ',', 'TEST ({1} - {0})')
        self.assertEqual('TEST (secondArg - firstArg)\n', parser.supplant())

    def test_supplant_3_args_ok(self):
        parser = CsvSupplant(self.sourceFile.name, ',', 'TEST ({1} - {0} - {2})')
        self.assertEqual('TEST (secondArg - firstArg - thirdArg)\n', parser.supplant())
    
    def test_supplant_index_out_of_range(self):
        parser = CsvSupplant(self.sourceFile.name, ',', 'TEST ({7} - {0})')
        self.assertRaises(IndexError, parser.supplant)
    
suite = unittest.TestLoader().loadTestsFromTestCase(CsvSupplantTest)
unittest.TextTestRunner(verbosity=2).run(suite)