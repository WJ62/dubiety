from distutils.core import setup

setup(
  name = 'dubiety',         # How you named your package folder (MyLib)
  packages = ['dubiety'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = """
                This package introduces a new type of object that permits the user to give, if desired, an uncertainty to a value. Plus, 
                you will have the ability to use these values in basic arithmetic calculations and have the uncertainty properly propagated 
                (with a non-uncertain and uncertain value). For more possible operations (such as the trigonometric ones [more to come in 
                the future]), use the dmath class of functions available through the package. The uncertainty is calculated following the 
                equations found in Data reduction and error analysis for the Physical Sciences by Philip R. Bevington and D. Keith Robinson 
                (McGraw-Hill).
                """,   # Give a short description about your library
  author = 'Wissem Jlassi',                   # Type in your name
  author_email = 'wj.f9812a.1@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/WJ62/dubiety',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/WJ62/dubiety/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['Uncertainties', 'Data reduction and error analysis for the physical sciences by Philip R. Bevington and D. Keith Robinson (McGraw-Hill)'],   # Keywords that define your package best
  install_requires=['numpy'],           # I get to this in a second
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10'
  ],
)
