import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='token_auth',  
     version='0.1',
     scripts=['token_auth'] ,
     author="Sharmad Tadkodkar",
     author_email="sharmadhonor6@gmail.com",
     description="jwt token verification code",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/samsonic221/token_auth",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )