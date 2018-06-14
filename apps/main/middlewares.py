#from django.shortcuts import redirect

#class Mymiddleware(object):
	#def process_request(self, request):
		#if request.user.is_authenticated():
#			if not request.user.is_superuser:
	#			paths = ['/', '/salir/']
		#		if request.path in paths:
			#		return None # no haga nada y deje que la peticion finalice
				#else:
					#return redirect('/') # no permita que la peticion continue y redireccione
				#	return None # POr el momento voy a permitir todas la peticiones
