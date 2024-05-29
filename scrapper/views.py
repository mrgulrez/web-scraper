import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import ExtractedData

@csrf_exempt
def extract_data(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title
        title = soup.title.string if soup.title else 'No title found'
        
        # Extract different types of data
        data = {
            'title': title,
            'headings': [heading.get_text() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
            'paragraphs': [p.get_text() for p in soup.find_all('p')],
            'lists': [[li.get_text() for li in ul.find_all('li')] for ul in soup.find_all('ul')],
            'images': [img['src'] for img in soup.find_all('img', src=True)],
            'links': [{'text': a.get_text(), 'href': a['href']} for a in soup.find_all('a', href=True)],
            'tables': []
        }

        # Extract table data
        for table in soup.find_all('table'):
            rows = []
            for row in table.find_all('tr'):
                cells = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                rows.append(cells)
            data['tables'].append(rows)

        # Save to database
        extracted_data = ExtractedData(
            url=url,
            title=title,
            content=str(data)  # Save the whole data dict as a string
        )
        extracted_data.save()

        return HttpResponseRedirect(reverse('view_data', args=[extracted_data.id]))
    
    return render(request, 'form.html')

def view_data(request, data_id):
    data = get_object_or_404(ExtractedData, id=data_id)
    content = eval(data.content)  
    return render(request, 'view_data.html', {'data': content, 'title': data.title, 'url': data.url})
