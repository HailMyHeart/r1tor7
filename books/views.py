# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request
from books.models import Book, Author
from django.http import HttpResponse, HttpResponseRedirect
def searchAndAdd(request):
    error_list = []
    year_list = []
    month_list = ['1','2','3','4','5','6','7','8','9','10','11','12']
    day_list = []
    for i in range(1990, 2050):
        year_list.append(str(i))
    for j in range(1, 32):
        day_list.append(str(j))
        
    book_list = Book.objects.all()    
    author_exist = True
    if request.method == 'POST':
        if author_exist:
            if not request.POST.get('ISBN',''):
                error_list.append('Enter the ISBN.')
            if not request.POST.get('Title',''):
                error_list.append('Enter the Title.')
            if not request.POST.get('AuthorName',''):
                error_list.append('Enter the Author Name.')
            else:
                if not Author.objects.filter(Name = request.POST['AuthorName']):
                    author_exist = False
                else:
                    author_exist = True
                            
            if not request.POST.get('Publisher',''):
                error_list.append('Enter the Publisher.')
            if not request.POST.get('Price',''):
                error_list.append('Enter the Price.')
        else:
            if not request.POST.get('AuthorAge',''):
                error_list.append('Enter the Author Age.')
            if not request.POST.get('AuthorCountry',''):
                error_list.append('Enter the Author Country.')
        if not error_list:
            if author_exist:
                if Author.objects.get(Name = request.POST['AuthorName']).Country =='0':
                    Author.objects.filter(Name = request.POST['AuthorName']).update(Country = request.POST['AuthorCountry'])
                    Author.objects.filter(Name = request.POST['AuthorName']).update(Age = request.POST['AuthorAge'])
                    
                Book.objects.create(ISBN = request.POST['ISBN'],Title = request.POST['Title'],AuthorID = Author.objects.get(Name = request.POST['AuthorName']),Publisher = request.POST['Publisher'],PublishDate = request.POST['year']+'-'+request.POST['month']+'-'+request.POST['day'],Price = request.POST['Price'] )
                return HttpResponseRedirect('/successful/')
            else:
                Author.objects.create(Name = request.POST['AuthorName'],Age = '0', Country = '0')
    return render_to_response('homepage.html', {'Price':request.POST.get('Price',''),'ISBN' :request.POST.get('ISBN',''), 'Title':request.POST.get('Title',''), 'AuthorName':request.POST.get('AuthorName',''), 'Publisher':request.POST.get('Publisher',''), 'author_exist':author_exist, 'error_list':error_list, 'year_list':year_list, 'month_list':month_list, 'day_list':day_list, 'book_list':book_list,})

def search_result(request):
    books_list=[]
    
    if request.method == 'POST':
        person = Author.objects.filter(Name = request.POST['search_author'])
        if person:
            books_list.extend(person[0].book_set.all())
    return render_to_response('search_result.html',{'books_list':books_list,} )

def show_book(request, ISBN):
    book = Book.objects.filter(ISBN = ISBN)
    if book:
        
        return render_to_response('book.html', {'book':book[0],})
    else:
        return render_to_response('book.html', {'book':book,})

def update_book(request, ISBN):
    Title = Book.objects.get(ISBN = ISBN).Title
    error_list = []
    year_list = []
    month_list = ['1','2','3','4','5','6','7','8','9','10','11','12']
    day_list = []
    for i in range(1990, 2050):
        year_list.append(str(i))
    for j in range(1, 32):
        day_list.append(str(j))
    author_exist = True
    if request.method == 'POST':
        if author_exist:
            if not request.POST.get('AuthorName',''):
                error_list.append('Enter the Author Name.')
            else:
                if not Author.objects.filter(Name = request.POST['AuthorName']):
                    author_exist = False
                            
            if not request.POST.get('Publisher',''):
                error_list.append('Enter the Publisher.')
            if not request.POST.get('Price',''):
                error_list.append('Enter the Price.')
        else:
            if not request.POST.get('AuthorAge',''):
                error_list.append('Enter the Author Age.')
            if not request.POST.get('AuthorCountry',''):
                error_list.append('Enter the Author Country.')
        if not error_list:
            if author_exist:
                if Author.objects.get(Name = request.POST['AuthorName']).Country =='0':
                    Author.objects.filter(Name = request.POST['AuthorName']).update(Country = request.POST['AuthorCountry'])
                    Author.objects.filter(Name = request.POST['AuthorName']).update(Age = request.POST['AuthorAge'])
                Book.objects.filter(ISBN = ISBN ).update(AuthorID=Author.objects.get(Name = request.POST['AuthorName']), Publisher = request.POST['Publisher'],PublishDate = request.POST['year']+'-'+request.POST['month']+'-'+request.POST['day'],Price = request.POST['Price']  )
                return HttpResponseRedirect('/successful/')
            else:
                Author.objects.create(Name = request.POST['AuthorName'], Age = '0', Country = '0')
    return render_to_response('update.html', {'Title':Title, 'ISBN':ISBN,'Price':request.POST.get('Price',''),  'AuthorName' :request.POST.get('AuthorName',''),'Publisher':request.POST.get('Publisher',''), 'author_exist':author_exist, 'error_list':error_list, 'year_list':year_list, 'month_list':month_list, 'day_list':day_list, })

def delete(request, ISBN):
    book_exist = False
    if Book.objects.filter(ISBN = ISBN):
        Book.objects.filter(ISBN = ISBN).delete()
        book_exist = True
    return render_to_response('delete.html', {'book_exist':book_exist,})

def successful(request):   
    return render_to_response('successful.html', {})     

    
    
            

            
                
            
            
                    
