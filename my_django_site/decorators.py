def first_decorater(view_func): #######if we need to build argument pass decorator than we have to write another function for it
    def decorator(request,*args,**kwargs):
        if request.method =='GET':
            print('GET request')
            return view_func(request,*args,**kwargs)
        else:
            print('not get request')
    return decorator