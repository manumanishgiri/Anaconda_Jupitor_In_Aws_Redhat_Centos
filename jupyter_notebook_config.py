c = get_config()

# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook

# Notebook config
c.NotebookApp.certfile = u'/home/ec2-user/certs/mycert.pem' #location of your certificate file
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False  #so that the ipython notebook does not opens up a browser by default
c.NotebookApp.password = u'sha1:262....your hash here.........65f'  #edit this with the SHA hash that you generated after typing in Step 9
# This is the port we opened in Step 3.
c.NotebookApp.port = 8888
