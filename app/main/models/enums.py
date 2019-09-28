from sqlalchemy import Enum

TEST = ('Enum1', 'Enum2', 'Enum3')
TEST_ENUM = Enum(*TEST, name='enum')
TEST_DICT = {
    'enum1': TEST[0],
    'enum2': TEST[1],
    'enum3': TEST[2],
}