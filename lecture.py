# from flask import Flask

# app=Flask(__name__)

# def make_bold_decorator(fun):
#     def wrapper():
#         content=fun()
#         return f'<strong>{content}</strong>'
#     return wrapper
# def make_italic_decorator(fun):
#     def wrapper():
#         content=fun()
#         return f'<em>{content}</em>'
#     return wrapper
# def make_underline_decorator(fun):
#     def wrapper():
#         content=fun()
#         return f'<u>{content}</u>'
#     return wrapper

# @app.route("/")
# @make_italic_decorator
# @make_underline_decorator
# @make_bold_decorator
# def hello():
#     return "hello world"

# @app.route("/name/<name>/<int:age>")
# def my_name(name, age):
#     return f"My name is {name} and I am {age} years old"

# @app.route('/cat')
# def fun():
#     return '<h1 style=text-align:center>My cat</h1>'\
#             '<p>Here is my cat</p>'\
#             '<img src="https://i.natgeofe.com/n/4cebbf38-5df4-4ed0-864a-4ebeb64d33a4/NationalGeographic_1468962_3x2.jpg?w=1638&h=1092"/>'

# if __name__=="__main__":
#     app.run(debug=True)