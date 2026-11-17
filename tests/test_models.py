from src.models.model_response_stats import ModelResponseStats

def test_model_response_stats():
    stats = ModelResponseStats(
        content_len=120,
        content_nbr_names=5,
        content_nbr_struct=2,
        content_nbr_correct_names=4,
        content_nbr_incorrect_names=1,
    )

    assert stats.content_len == 120
    assert stats.content_nbr_names == 5
    assert stats.content_nbr_struct == 2
    assert stats.content_nbr_correct_names == 4
    assert stats.content_nbr_incorrect_names == 1