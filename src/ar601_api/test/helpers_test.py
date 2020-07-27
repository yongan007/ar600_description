import unittest
from ar601_api.helpers import JointStatesWrapper
from ar601_api.constants import max_radian_per_tick


def create_type(type_name, **kwargs):
    return type(type_name, (object,), kwargs)


def init_js_wrapper():
    js_msg = create_type('joint_states', name=['joint1', 'joint2'], position=[5.55, 4.62])
    return JointStatesWrapper(js_msg)


class TestJointStatesWrapper(unittest.TestCase):
    def test_positions_success(self):
        self.assertEqual(4.62, init_js_wrapper().position('joint2'))

    def test_positions_failed(self):
        with self.assertRaises(KeyError) as ctx:
            init_js_wrapper().position('joint3')
        self.assertIn("not found in names", str(ctx.exception))


class TestMaxRadianPerTick(unittest.TestCase):
    def test_positions_success(self):
        self.assertAlmostEqual(0.056, max_radian_per_tick(300), places=5)
        self.assertAlmostEqual(0.052, max_radian_per_tick(750), places=5)
        self.assertAlmostEqual(0.039, max_radian_per_tick(1100), places=5)
        self.assertAlmostEqual(0.02, max_radian_per_tick(2500), places=5)
        self.assertAlmostEqual(0.018, max_radian_per_tick(3500), places=5)


if __name__ == '__main__':
    unittest.main()
