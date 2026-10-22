from chemistry.tick import Chemical, snapshot, tick


def test_tick_decays_toward_baseline():
    chem = Chemical(name="dopamine", baseline=50.0, half_life_seconds=60.0, current=100.0)
    tick({"dopamine": chem}, dt_seconds=60.0)
    assert abs(chem.current - 75.0) < 0.01


def test_snapshot_rounds():
    chem = Chemical(name="x", baseline=50.0, half_life_seconds=60.0, current=50.12345)
    assert snapshot({"x": chem})["x"] == 50.12