from setuptools import setup, find_packages

setup(name='app', packages= find_packages(include=['app', 'app.*']),
install_requires=[
  'async-exit-stack==1.0.1',
  'async-generator==1.10',
  'bcrypt==3.2.0',
  'cffi==1.14.4',
  'click==7.1.2',
  'cryptography==3.3.1',
  'ecdsa==0.14.1',
  'fastapi==0.63.0',
  'h11==0.12.0',
  'motor==2.3.0',
  'passlib==1.7.4',
  'psycopg2-binary==2.8.6',
  'pyasn1==0.4.8',
  'pycparser==2.20',
  'pydantic==1.7.3',
  'pymongo==3.11.2',
  'python-jose==3.2.0',
  'rsa==4.7',
  'six==1.15.0',
  'SQLAlchemy==1.3.22',
  'SQLAlchemy-Utils==0.36.8',
  'starlette==0.13.6',
  'uvicorn==0.13.3',
  ]
 )