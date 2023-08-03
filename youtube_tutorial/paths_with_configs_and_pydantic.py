import pydantic 
import yaml 
from pathlib import Path 


class PydanticSettings(pydantic.BaseModel):
    path: Path # Read in yaml and specify the path as a PATH object
    other: str 


path = Path.cwd() / "file.yaml"
parsed_yaml = yaml.safe_load(path.read_text())
settings = PydanticSettings(**parsed_yaml)
print(settings)
print(settings.path.parent)