# this is your project's setup.py script
#python setup.py sdist upload 

import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

from setuptools import setup


class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')
setup(name='pypollution',
      version='1.0',
      description='Python machine learning ocr.',
      author='Prashant Kumar',
      author_email='kr.prashant94@gmail.com',
      license='MIT',
      packages=['pypollution'],
      zip_safe=False,
      cmdclass={
        'register': register,
        'upload': upload,
    })