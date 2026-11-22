import pytest
import render.lod_skirt_blend as mod

CASES = [
    ("skirt_both_ends", (1, 2)),
    ("attribute_normalize", (1, 2)),
    ("forced_rebuild", (1, 2)),
    ("neighbor_sample", (1, 2)),
    ("crack_distance", (1.0, 2.0)),
    ("quadtree_split", (1, 2)),
    ("frustum_edge", (1, 2)),
    ("height_bias", (0.5, 0.2)),
    ("temporal_hysteresis", (3, 2)),
    ("border_match", (1, 2)),
    ("index_remap", (1, 2)),
    ("normal_blend", (1, 2)),
    ("skirt_height", (0.5, 1.0)),
    ("transition_frame", (1, 2)),
    ("crack_metric", (0.001, 0.002)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
