import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name= 'car.io',
    options={'build_exe':{'pacages':['pygame'],'include_files':['lambo.png'],['flame.png']}},
    executables = executables
)