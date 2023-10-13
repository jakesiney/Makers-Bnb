from lib.space_repository import SpaceRepository
from lib.space import Space
from datetime import date


def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1,'House_1', 'nice house', 150.00, date(2023,1,1), date(2023,10,1), 1),
        Space(2,'House_2', 'nice pool', 250.00, date(2023,4,1), date(2023,9,1), 2),
        Space(3,'House_3', 'nice garden', 350.00, date(2023,6,1), date(2023,11,1), 3)
    ]
def test_create_a_space(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = SpaceRepository(db_connection)
    repository.create(Space(None,'House_4','nice porch', 300.00, date(2023,10,5),date(2023,11,4),2))
    spaces = repository.all()
    assert spaces == [
        Space(1, 'House_1', 'nice house', 150.00, date(2023,1,1), date(2023,10,1), 1),
        Space(2, 'House_2', 'nice pool', 250.00, date(2023,4,1),date(2023,9,1), 2),
        Space(3, 'House_3', 'nice garden', 350.00,date(2023,6,1), date(2023,11,1), 3),
        Space(4, 'House_4','nice porch', 300.00, date(2023,10,5),date(2023,11,4),2)
    ]

# def test_delete_a_space(db_connection):
#     db_connection.seed('seeds/makers_bnb.sql')
#     repository = SpacesRepository(db_connection)
#     repository.delete('House_1')
#     assert repository.all == [Space('House_2', 'nice pool', 250.00, date(2023,4,1),date(2023,9,1), 2),
#                               Space('House_3', 'nice garden', 350.00,date(2023,6,1), date(2023,11,1), 3),
#     ]