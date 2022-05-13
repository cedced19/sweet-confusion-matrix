import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='sweetconfusionmatrix',  
     version='0.1',
     author="Cédric Jung",
     author_email="cedced19@gmail.com",
     description="A tool to generate sweet confusion matrix",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/cedced19/sweet-confusion-matrix",
     packages=setuptools.find_packages(),
     install_requires=["matplotlib", "seaborn", "sklearn", "pandas", "numpy"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )