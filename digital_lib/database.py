from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from digital_lib.models import Base
DATABASE_CONFIG = ('sqlite', '///', 'digital_library.db')
engine = create_engine(f'{DATABASE_CONFIG[0]}:{DATABASE_CONFIG[1]}{DATABASE_CONFIG[2]})