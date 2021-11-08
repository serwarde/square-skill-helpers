from setuptools import setup

setup(
    name="square_skill_helpers",
    version="0.0.1",    
    description="",
    url="www.informatik.tu-darmstadt.de/ukp",
    author="UKP",
    author_email="baumgaertner@ukp.informatik.tu-darmstadt.de",
    packages=["square_skill_helpers"],
    install_requires=[
        "requests==2.26.0",
        "numpy==1.21.3",                     
        "python-dotenv==0.19.1 ",                     
    ],
)
