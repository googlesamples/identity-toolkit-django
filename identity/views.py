from os import path
import json
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from identitytoolkit import gitkitclient

server_config_json = path.join(path.dirname(path.realpath(__file__)), '../gitkit-server-config.json')
gitkit_instance = gitkitclient.GitkitClient.FromConfigFile(server_config_json)

widget_config_json = path.join(path.dirname(path.realpath(__file__)), 'widget_config.json')
f = open(widget_config_json)
widget_config = json.loads(f.read())
f.close()

def index(request):
	text = "You are not signed in."

	if 'gtoken' in request.COOKIES:
		gitkit_user = gitkit_instance.VerifyGitkitToken(request.COOKIES['gtoken'])
		if gitkit_user:
			text = "Welcome " + gitkit_user.email + "! Your user info is: " + str(vars(gitkit_user))


	context = {'CONTENT': text}
	return render(request, 'identity/index.html', context)

def widget(request):
	context = {
		'apiKey': widget_config['apiKey']
	}
	return render(request, 'identity/widget.html', context)