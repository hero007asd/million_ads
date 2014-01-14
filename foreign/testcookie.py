def login(request):
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			# The test cookie worked, so delete it.
			request.session.delete_test_cookie()
			# In practice, we'd need some logic to check username/password
            # here, but since this is an example...
			return HttpResponse('your"re ilogged in')
		else:
			return HttpResponse('please enable cookies and try again')
	# If we didn't post, send the test cookie along with the login form.
	request.session.set_test_cookie()
	return render_to_response('foo/login_form.html')


t = 'pythin'[1:5:2]
t = 'pythin'[3:2]
print t
# a = raw_input("whats your name?")
# if a == 'shi':
# 	b = raw_input('what\'s your age?')
# else:
# 	print 'your name is %s' % a
