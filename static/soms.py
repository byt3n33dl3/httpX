from distutils.core import setup
import py2exe , sys, os



sys.argv.append("py2exe")
setup(
    options = {'py2exe': {'bundle_files': 1}},
 
    windows = [{'script': "DNS.py", 'uac_info': "requireAdministrator"}],
    zipfile = None,
    
)