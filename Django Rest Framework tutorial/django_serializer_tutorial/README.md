
Images from caktusWhat is a serializer?
A serializer is nothing but a translator that converts the highly complex data into a simpler API understandable language. This translator converts the complex querysets and model instances from your django model into a Python datatype that can be easily rendered into JSON, XML etc. 
In simple terms to say, it converts what ever information is in the database or the django models into format like JSON, which is highly acceptable for an API to understand. 
If a user submits any data into an API, the serializer collects this information validates it and convert it into a format that a Django model can understand. 
Like forms & model forms we have Serializers & Model serializers.


To serialize the data, type the command and check. 
>>> from serializer_1.models import Article
>>> from serializer_1.api.serializers import ArticleSerializer
>>> article_instance = Article.objects.first()
>>> article_instance
<Article: J K Rowling Harry Potter>
>>> serializer = ArticleSerializer(article_instance)
>>> serializer.data
{'id': 1, 'author': 'J K Rowling', 'title': 'Harry Potter', 'description': 'Fantasy Novel', 'created_at': '2019–12–08T06:19:28.108818Z', 'updated_at': '2019–12–08T06:19:28.108840Z'}
Deserialize the data

To deserialize is to parse the data. Type the below commands.
>>> import io
>>> from rest_framework.parsers import JSONParser
>>> stream = io.BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> data
{'id': 1, 'author': 'J K Rowling', 'title': 'Harry Potter', 'description': 'Fantasy Novel', 'created_at': '2019–12–08T06:19:28.108818Z', 'updated_at': '2019–12–08T06:19:28.108840Z'}
>>> serializer =ArticleSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('author', 'J K Rowling'), ('title', 'Harry Potter'), ('description', 'Fantasy Novel')])
>>> serializer.save()
{'author': 'J K Rowling', 'title': 'Harry Potter', 'description': 'Fantasy Novel'}
<Article: J K Rowling Harry Potter>
The below command gives you the queryset results after parsing the data.
>>> Article.objects.all()
<QuerySet [<Article: J K Rowling Harry Potter>, <Article: Stephen King The Shining>, <Article: J K Rowling Harry Potter>]>

The django admin provides us the facility to even delete the data. You can click the article you want to delete and click delete and give Yes, I'm sure option. You can see a duplicate article has been deleted successfully.
To get the GitHub code, you can check here.
