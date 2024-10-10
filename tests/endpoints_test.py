from database.connect import accidents_collection, monthly_collection
from repository.utils import find_the_day, find_the_week





def test_get_accidents_by_area():
    accidents = list(accidents_collection.find({'BEAT_OF_OCCURRENCE': '1654'}))
    assert accidents


def test_get_accidents_by_cause():
    pipeline = [
        {'$match': {'BEAT_OF_OCCURRENCE': '1654'}},
        {'$group': {
            '_id': '$PRIM_CONTRIBUTORY_CAUSE',
            'count': {'$sum': 1}
        }}
    ]
    results = list(accidents_collection.aggregate(pipeline))
    assert results


def test_get_injury_statistics():
    pipeline = [
        {'$match': {'BEAT_OF_OCCURRENCE': '1654'}},
        {'$group': {
            '_id': None,
            'total_injuries': {'$sum': '$injuries.INJURIES_TOTAL'},
            'fatal_injuries': {'$sum': '$injuries.fatal'},
            'non_fatal_injuries': {'$sum': '$injuries.non_fatal'}
        }}
    ]
    stats = accidents_collection.aggregate(pipeline)
    assert stats

def test_get_accidents_by_area_and_date():
    day_accidents =  find_the_day('04-04-2020', '1654')
    assert day_accidents



def test_get_accidents_by_area_and_month():
    month_accidents =  { 'area':'225', 'month': 9}
    my_month_res = monthly_collection.find_one(month_accidents)
    assert my_month_res



def test_get_accidents_by_area_and_week():
    week_accidents =  find_the_week('09-18-2023', '411')
    assert week_accidents
