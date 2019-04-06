from find_clusters.find_clusters import find_clusters


def test_find_clusters():
    arr = [
        [1, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1]
    ]
    assert find_clusters(arr) == [7, 2, 1, 5, 2]
