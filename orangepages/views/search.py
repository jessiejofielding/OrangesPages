from flask import request, make_response
from flask import Blueprint, render_template
from orangepages.models.models import User, Tag
from orangepages.views.util import render


page = Blueprint('testsearch', __name__)



@page.route('/search')
def search_user():
    query_list = request.args.get('query').split(' ')

    # FIXME sry - zx

    posts = search_tag(query_list)
    user_preview_list = User.search(*query_list).all()
    query = ' '.join(query_list)

    return render('test/all_posts.html', posts=posts,
    user_preview_list=user_preview_list, query=query, count=len(user_preview_list))

# helper method
def search_tag(query_list):
    tagged_posts = []
    for query in query_list:
        print("hash", query)

        tag = Tag.query.get(query)
        if tag == None:
            posts = []
        else:
            posts = tag.get_posts()

        tagged_posts.extend(posts)

    return tagged_posts

# @page.route('/searchbar-tag')
# def searchbar_tag():
#     return render('test/searchbar-tag.html')
