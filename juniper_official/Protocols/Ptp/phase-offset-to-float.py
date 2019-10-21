'''
This function converts a ptp-spll-phase-offset string with some text to a float
'''


def string_to_float(phase_offset, **kwargs):
    if phase_offset.endswith(' sec'):
        phase_offset = phase_offset[:-4]
    return float(phase_offset)


def test_conversion():
    assert string_to_float(
        "-0.000000013 sec") == float(-0.000000013), "Should be -0.000000013"


if __name__ == "__main__":
    test_conversion()
    print("Everything passed")
