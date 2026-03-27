from app.database import engine
from app.models import Base
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Base.metadata.create_all(bind=engine)