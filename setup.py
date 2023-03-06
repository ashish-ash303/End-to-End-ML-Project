from setuptools import find_packages,setup
from typing import List



hypen='-e .'
def get_requirement(file_path:str)->List[str]:
    "this Function will return the list of requirement"

    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)

    return requirements





setup(
    name="first_ml_project",
    version='0.0.1',
    author="Ashish Srivastav",
    author_email='ashish@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')

)