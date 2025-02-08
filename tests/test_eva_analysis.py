import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

...

def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns expected ground truth values
    for typical crew values
    """
    actual_result = calculate_crew_size("Valentina Tereshkova;")
    expected_result = 1
    assert actual_result == expected_result

    actual_result = calculate_crew_size("Judith Resnik; Sally Ride;")
    expected_result = 2
    assert actual_result == expected_result

# Edge cases
def test_calculate_crew_size_edge_cases():
    """
    Test that calculate_crew_size returns expected ground truth values
    for edge case where crew is an empty string
    """
    actual_result = calculate_crew_size("")
    assert actual_result is None