import unittest

from unittest import mock

from prediction import SomeModel, predict_message_mood


class TestSomeModel(unittest.TestCase):
    def setUp(self):
        self.test_model = SomeModel()

    def test_bad_marks(self):
        with mock.patch("prediction.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.1
        self.assertEqual(predict_message_mood(None, mock_predict()), "неуд")

    def test_good_marks(self):
        with mock.patch("prediction.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.3
        self.assertEqual(predict_message_mood(None, mock_predict()), "норм")

    def test_excellent_marks(self):
        with mock.patch("prediction.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.9
        self.assertEqual(predict_message_mood(None, mock_predict()), "отл")

    def test_out_border_values(self):
        with mock.patch("prediction.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 1
        self.assertEqual(predict_message_mood(None, mock_predict()), "отл")

    def test_inner_border_values(self):
        with mock.patch("prediction.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.3
        self.assertEqual(predict_message_mood(None, mock_predict()), "норм")

