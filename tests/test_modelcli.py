# -*- coding: utf-8 -*-
import pdb
import unittest

from click.testing import CliRunner

from nseta.cli.modelcli import create_cdl_model

class TestModelcli(unittest.TestCase):
	def setUp(self):
		pass

	def test_create_cdl_model(self):
		runner = CliRunner()
		result = runner.invoke(create_cdl_model, args=['--symbol', 'BANDHANBNK', '--start', '2020-01-01', '--end', '2020-01-08', '--steps', '--clear'])
		self.assertEqual(result.exit_code , 0)
		self.assertIn("Model saved to: BANDHANBNK.csv", result.output, str(result.output))
		self.assertIn("Candlestick pattern model plot saved to: BANDHANBNK_candles.html", result.output, str(result.output))

	def test_create_cdl_model_inputs(self):
		runner = CliRunner()
		result = runner.invoke(create_cdl_model, args=['--start', '2020-01-01', '--end', '2020-01-08', '--steps', '--clear'])
		self.assertEqual(result.exit_code , 0)
		self.assertIn("Usage:  [OPTIONS]", result.output, str(result.output))

	def test_create_cdl_model_pickle(self):
		runner = CliRunner()
		result = runner.invoke(create_cdl_model, args=['--symbol', 'BANDHANBNK', '--start', '2020-01-01', '--end', '2020-01-08', '--format', 'pkl'])
		self.assertEqual(result.exit_code , 0)
		self.assertIn("Model saved to: BANDHANBNK.pkl", result.output, str(result.output))
		self.assertIn("Candlestick pattern model plot saved to: BANDHANBNK_candles.html", result.output, str(result.output))

	def tearDown(self):
	  pass

if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(TestModelcli)
	result = unittest.TextTestRunner(verbosity=2).run(suite)
	if six.PY2:
		if result.wasSuccessful():
			print("tests OK")
		for (test, error) in result.errors:
			print("=========Error in: %s===========" % test)
			print(error)
			print("======================================")

		for (test, failures) in result.failures:
			print("=========Error in: %s===========" % test)
			print(failures)
			print("======================================")