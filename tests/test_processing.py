import pytest

from src.processing import filter_by_state, sort_by_date


# параметризированный тест для функции filter_by_state
@pytest.mark.parametrize("lst, state, expected", [
    ([
         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": 5, "state": "CANCELED"},
     ],
     "EXECUTED",
     [
         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
     ]),

    ([
         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": 5, "state": "CANCELED"},
     ],
     "CANCELED",
     [
         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": 5, "state": "CANCELED"},
     ]),

    ([
         {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
         {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": 5, "state": "CANCELED"},
     ],
     "EXECUTED",
     []
    ),
    ])
def test_filter_by_state_parametrize(lst, state, expected):
    assert filter_by_state(lst, state) == expected


# параметризированный тест для функции sort_by_date
@pytest.mark.parametrize("lst, key_sort, expected", [
    (
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
    True,
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    ),
(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
    False,
    [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    ),
(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ],
    True,
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    ),
])
def test_sort_by_date(lst, key_sort, expected):
    assert sort_by_date(lst, key_sort) == expected