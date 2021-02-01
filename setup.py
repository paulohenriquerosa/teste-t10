from setuptools import setup, find_packages

setup(name='app', packages= find_packages(include=['app', 'app.*']),
install_requires=[
  'async-exit-stack==1.0.1',
  'async-generator==1.10',
  'click==7.1.2',
  'fastapi==0.63.0',
  'h11==0.12.0',
  'motor==2.3.0',
  'pydantic==1.7.3',
  'pymongo==3.11.2',
  'SQLAlchemy==1.3.22',
  'starlette==0.13.6',
  'uvicorn==0.13.3',
  ]
 )