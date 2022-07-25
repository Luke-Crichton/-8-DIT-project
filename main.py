from deepface import DeepFace
import pandas as pd
from deepface.commons import realtime
DeepFace.stream(db_path = r"C:/Users/lukec/test/empty", model_name='DeepFace', source=0, time_threshold=10, frame_threshold=20)