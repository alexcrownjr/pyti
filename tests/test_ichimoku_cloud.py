import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import ichimoku_cloud


class TestIchimokuCloud(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.close_data = SampleData().get_sample_close_data()
        self.high_data = SampleData().get_sample_high_data()
        self.low_data = SampleData().get_sample_low_data()
        self.volume = SampleData().get_sample_volume()

        self.tenkansen_default_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 803.82500000000005, 809.03999999999996,
        810.11000000000001, 812.84500000000003, 812.84500000000003,
        812.89499999999998, 812.89499999999998, 806.52999999999997,
        804.68000000000006, 797.03499999999997, 797.03499999999997,
        791.17499999999995, 789.83500000000004, 786.8900000000001,
        786.8900000000001, 779.75, 777.90000000000009, 776.88499999999999,
        776.88499999999999, 776.88499999999999, 776.88499999999999,
        782.66000000000008, 782.70500000000004, 780.65999999999997,
        769.69000000000005, 769.69000000000005, 769.69000000000005,
        779.40499999999997, 782.60000000000002, 782.60000000000002,
        782.60000000000002, 782.60000000000002, 782.60000000000002,
        791.86500000000001, 796.13499999999999, 800.32999999999993,
        800.32999999999993, 801.60000000000002, 804.82500000000005,
        808.96500000000003, 812.07999999999993, 820.61000000000001,
        822.81999999999994, 826.54500000000007, 821.28999999999996,
        820.17000000000007, 819.91000000000008, 819.91000000000008,
        815.58500000000004, 815.58500000000004, 813.90000000000009,
        811.10000000000002, 807.44000000000005, 807.44000000000005,
        807.27499999999998, 807.27499999999998, 807.27499999999998,
        807.27499999999998, 805.55500000000006, 805.55500000000006,
        807.67000000000007, 808.16499999999996, 808.16499999999996,
        807.86500000000001, 805.67000000000007, 805.67000000000007,
        805.67000000000007, 803.20500000000004, 802.33500000000004,
        802.33500000000004, 796.755, 795.66000000000008, 798.23500000000001,
        798.25, 798.25, 798.25, 798.25, 798.25, 798.25, 798.93499999999995,
        798.93499999999995, 798.93499999999995, 793.36000000000001,
        793.40000000000009, 794.75, 797.02499999999998, 798.3599999999999,
        798.3599999999999, 798.63, 800.32500000000005, 802.39499999999998,
        802.72000000000003, 804.06999999999994, 804.84000000000003,
        804.84000000000003, 802.87, 802.87, 802.87, 802.87, 799.91499999999996,
        786.66000000000008, 784.45000000000005, 782.28999999999996,
        779.23000000000002, 779.23000000000002, 777.67499999999995,
        777.67499999999995, 772.375, 759.51999999999998, 748.79999999999995,
        747.45499999999993, 744.38, 744.38, 742.1400000000001,
        737.43000000000006, 730.33500000000004, 730.23000000000002,
        720.34500000000003, 720.34500000000003]


        self.kijunsen_default_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 791.11000000000001, 791.11000000000001,
        791.11000000000001, 791.11000000000001, 791.11000000000001,
        791.11000000000001, 791.11000000000001, 785.55500000000006,
        785.55500000000006, 785.55500000000006, 785.55500000000006,
        785.55500000000006, 784.27999999999997, 782.60000000000002,
        782.60000000000002, 782.60000000000002, 782.60000000000002,
        782.60000000000002, 786.38999999999999, 786.38999999999999,
        787.66000000000008, 790.88499999999999, 794.48000000000002,
        794.48000000000002, 794.48000000000002, 794.48000000000002,
        794.48000000000002, 794.48000000000002, 794.48000000000002,
        794.48000000000002, 794.48000000000002, 794.48000000000002,
        794.48000000000002, 803.745, 808.01499999999999, 808.42000000000007,
        808.42000000000007, 808.42000000000007, 808.42000000000007,
        808.96500000000003, 812.07999999999993, 818.05999999999995,
        818.05999999999995, 818.05999999999995, 818.05999999999995,
        818.05999999999995, 817.75999999999999, 815.56500000000005,
        811.24000000000001, 811.24000000000001, 808.77500000000009,
        805.10500000000002, 802.33500000000004, 802.21500000000003,
        802.21500000000003, 802.21500000000003, 802.21500000000003,
        802.21500000000003, 802.21500000000003, 802.21500000000003,
        802.21500000000003, 802.21500000000003, 802.21500000000003,
        802.21500000000003, 802.21500000000003, 802.21500000000003,
        802.21500000000003, 802.21500000000003, 802.21500000000003,
        802.21500000000003, 798.25, 798.25, 798.25, 798.34000000000003,
        798.48500000000001, 798.48500000000001, 798.48500000000001,
        798.48500000000001, 798.48500000000001, 799.17000000000007,
        799.17000000000007, 799.17000000000007, 799.17000000000007,
        787.16499999999996, 785.23000000000002, 783.06999999999994,
        783.005, 783.005, 781.45000000000005, 781.45000000000005,
        780.95000000000005, 780.84500000000003, 772.05999999999995,
        772.05999999999995, 768.98500000000001, 768.98500000000001,
        767.84500000000003, 763.13499999999999, 757.875, 757.875,
        756.18499999999995, 755.90999999999997]

        self.chiku_span_expected = [779, 785, 784.8, 775.97, 786.16, 779.98,
        775.16, 753.22, 771.75, 780.29, 805.59, 811.98, 802.03, 781.1, 782.19,
        788.42, 805.48, 809.9, 819.56, 817.35, 822.1, 828.55, 835.74, 824.06,
        821.63, 827.09, 821.49, 806.84, 804.6, 804.08, 811.77, 809.57, 814.17,
        800.71, 803.08, 801.23, 802.79, 800.38, 804.06, 802.64, 810.06, 810.73,
        802.65, 814.96, 815.95, 805.03, 799.78, 795.39, 797.97, 801.23, 790.46,
        788.72, 798.82, 788.48, 802.84, 807.99, 808.02, 796.87, 791.4, 789.85,
        791.92, 795.82, 793.22, 791.3, 793.6, 796.59, 796.95, 799.65, 802.75,
        805.42, 801.19, 805.96, 807.05, 808.2, 808.49, 807.48, 805.23, 806.93,
        797.25, 798.92, 800.12, 800.94, 791.34, 765.84, 761.97, 757.65, 757.52,
        759.28, 754.41, 757.08, 753.41, 753.2, 735.63, 735.8, 729.48, 732.51,
        727.2, 717.78, 707.26, 708.97, 704.89, 710.25]

        self.senkou_a_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, 783.9975, 783.9975, 783.9975, 783.9975, 786.885, 786.9075,
        785.885, 777.6225000000001, 777.6225000000001, 777.6225000000001,
        782.48, 784.0775000000001, 783.44, 782.6, 782.6, 782.6,
        787.2325000000001, 789.3675000000001, 793.3599999999999,
        793.3599999999999, 794.6300000000001, 797.855, 801.7225000000001,
        803.28, 807.5450000000001, 808.65, 810.5125, 807.885, 807.325, 807.195,
        807.195, 805.0325, 805.0325, 808.8225, 809.5575, 807.9300000000001,
        807.9300000000001, 807.8475000000001, 807.8475000000001, 808.12,
        809.6775, 811.8075, 811.8075, 812.865, 813.1125, 813.1125, 812.8125,
        810.6175000000001, 808.455, 808.455, 805.99, 803.72, 802.335, 799.485,
        798.9375, 800.225, 800.2325000000001, 800.2325000000001,
        800.2325000000001, 800.2325000000001, 800.2325000000001,
        800.2325000000001, 800.575, 800.575, 800.575, 797.7875,
        797.8075000000001, 798.4825000000001, 799.62, 800.2874999999999,
        798.305, 798.44, 799.2875, 800.3675000000001, 800.6025,
        801.2774999999999, 801.6625, 801.6625, 800.6775, 801.02, 801.02,
        801.02, 799.5425, 786.9125, 784.84, 782.68, 781.1175000000001,
        781.1175000000001, 779.5625, 779.5625, 776.6625, 770.1825, 760.43,
        759.7574999999999, 756.6825, 756.6825, 754.9925000000001, 750.2825,
        744.105, 744.0525, 738.265, 738.1275]

        self.senkou_b_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48,
        794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48,
        794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 794.48,
        794.48, 794.48, 794.48, 794.48, 794.48, 794.48, 803.745, 808.015,
        808.4200000000001, 808.4200000000001, 808.4200000000001,
        808.4200000000001, 808.965, 812.0799999999999, 812.11, 812.11, 812.11,
        812.11, 812.11, 812.11, 812.11, 807.7850000000001, 807.7850000000001,
        807.7850000000001, 804.985, 802.215, 802.215, 802.215, 802.215,
        802.215, 790.895, 788.96, 786.8, 786.735, 786.735, 785.1800000000001,
        785.1800000000001, 784.6800000000001, 784.575, 775.79, 775.79, 772.715,
        772.715, 767.845, 763.135, 757.875, 757.875, 756.69, 756.69]

    def test_tenkansen_default_period(self):
        ts = ichimoku_cloud.tenkansen(self.close_data)
        np.testing.assert_array_equal(ts, self.tenkansen_default_expected)

    def test_kijunsen_default_period(self):
        ks = ichimoku_cloud.kijunsen(self.close_data)
        np.testing.assert_array_equal(ks, self.kijunsen_default_expected)

    def test_chiku_span(self):
        cs = ichimoku_cloud.chiku_span(self.close_data)
        np.testing.assert_array_equal(cs, self.chiku_span_expected)

    def test_senkou_a(self):
        sa = ichimoku_cloud.senkou_a(self.close_data)
        np.testing.assert_array_equal(sa, self.senkou_a_expected)

    def test_senkou_b(self):
        sb = ichimoku_cloud.senkou_b(self.close_data)
        np.testing.assert_array_equal(sb, self.senkou_b_expected)
