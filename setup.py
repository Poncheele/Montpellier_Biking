from setuptools import setup

setup(
  name='montpellier_biking',
  version='0.0.1',
  description='Visualization of the bicycle flux in Montpellier',
  url='https://github.com/Poncheele/Montpellier_Biking',
  author='Alleau Julie, Chaoui Wiam, Poncheele Clement et Seck, Gade',
  author_email='julie.alleau@etu.umontpellier.fr, wiam.chaoui@etu.umontpellier.fr, clement.poncheele@etu.umontpellier.fr et gade.seck@etu.umontpellier.fr',
  license='MIT',
  packages=['montpellier_biking','montpellier_biking.io', 'montpellier_biking.model', 'montpellier_biking.vis'],
  zip_safe=False
)

