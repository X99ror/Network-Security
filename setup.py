from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    return List[str]: description
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read Lines from the files
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip() ## removing the empty spaces
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requiremnts.txt not found")
        
    return requirement_lst
print(get_requirements())
setup(
    name="Netork security",
    version="0.0.0.1",
    author="Himanshu Raj",
    author_email="rajhimanshu4321@gmail.com",
    packages=find_packages()
    
)
    
            