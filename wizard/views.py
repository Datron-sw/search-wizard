from django.shortcuts import render, redirect
from .forms import SearchQueryForm
from django.http import JsonResponse
from urllib.parse import urlencode

def home_redirect(request):
    return redirect('/google/')


def tarayici_seçimi(request):
    if request.method == 'POST':  
        form = SearchQueryForm(request.POST)
        
        if form.is_valid():
            selected_engine = form.cleaned_data['search_engine']           
            params = {
                'search_input': form.cleaned_data['search_input'],
                'file_type': form.cleaned_data.get('file_type', ''),
                'selected_site': form.cleaned_data.get('selected_site', ''),
                'search_type': form.cleaned_data['search_type'],
                'selected_language':form.cleaned_data['selected_language']
            }
            query_string = urlencode(params)           
            
            if selected_engine == 'yandex':
                return redirect(f'/yandex/?{query_string}')
            if selected_engine == 'brave':
                return redirect(f'/brave/?{query_string}')
            if selected_engine == 'google':
                return redirect(f'/google/?{query_string}')
            if selected_engine == 'edge':
                return redirect(f'/edge/?{query_string}')
            if not selected_engine:
                    bolunmus_url = request.META.get('HTTP_REFERER', '/').split("/")
                    query = form.cleaned_data['search_input']  

                    file_type = form.cleaned_data['file_type']
                    
                    site = form.cleaned_data['selected_site']

                    arama_türü = form.cleaned_data['search_type']
                      
                    dil = form.cleaned_data['selected_language']

                    dork=""

                    if query:       
                        dork += f'intitle:"{query}"'
                    
                    if file_type:
                        dork += f' filetype:{file_type}'
                            
                    if site:
                        dork += f' site:{site}'

                    if arama_türü: 
                        dork += f' inurl:{arama_türü}'
                
                    if arama_türü == "image":
                            if  bolunmus_url[3] == "google" :
                                url = f"https://www.google.com/search?tbm=isch&q={query}"
                            if  bolunmus_url[3] == "yandex" :
                                url = f"https://yandex.com/images/search?text={query}"
                            if  bolunmus_url[3] == "brave" :
                                url = f"https://search.brave.com/images?q={query}"
                            if  bolunmus_url[3] == "edge" :
                                url =  f"https://www.bing.com/images/search?q={query}"

                    if arama_türü != "image":
                        if dil == "türkçe":
                            if bolunmus_url[3] == "google":        
                                url = f"https://www.google.com/search?q={dork}&hl=tr"
                            if bolunmus_url[3] == "yandex":  
                                url = f"https://yandex.com/search/?text={dork}&lang=tr"
                            if bolunmus_url[3] == "brave":  
                                url = f"https://search.brave.com/search?q={dork}&hl=tr"
                            if bolunmus_url[3] == "edge":  
                                url = f"https://www.bing.com/search?q={dork}&setlang=tr"   
                        if dil == "ingilizce":
                            if bolunmus_url[3] == "google":        
                                url = f"https://www.google.com/search?q={dork}&hl=en"
                            if bolunmus_url[3] == "yandex":  
                                url = f"https://yandex.com/search/?text={dork}&lang=en"
                            if bolunmus_url[3] == "brave":  
                                url = f"https://search.brave.com/search?q={dork}&hl=en"
                            if bolunmus_url[3] == "edge":  
                                url = f"https://www.bing.com/search?q={dork}&setlang=en" 
                        if dil == "fransizca":
                            if bolunmus_url[3] == "google":        
                                url = f"https://www.google.com/search?q={dork}&hl=fr"
                            if bolunmus_url[3] == "yandex":  
                                url = f"https://yandex.com/search/?text={dork}&lang=fr"
                            if bolunmus_url[3] == "brave":  
                                url = f"https://search.brave.com/search?q={dork}&hl=fr"
                            if bolunmus_url[3] == "edge":  
                                url = f"https://www.bing.com/search?q={dork}&setlang=fr" 
                        if dil == "almanca":
                            if bolunmus_url[3] == "google":        
                                url = f"https://www.google.com/search?q={dork}&hl=de"
                            if bolunmus_url[3] == "yandex":  
                                url = f"https://yandex.com/search/?text={dork}&lang=de"
                            if bolunmus_url[3] == "brave":  
                                url = f"https://search.brave.com/search?q={dork}&hl=de"
                            if bolunmus_url[3] == "edge":  
                                url = f"https://www.bing.com/search?q={dork}&setlang=de" 
                    
                    return JsonResponse({'redirect_url': url})
            
def google(request):
    form =  SearchQueryForm(request.GET or None) 
    return render(request, 'wizard/Google.html', {'form': form})

def yandex(request):
    form = SearchQueryForm(request.GET or None) 
    return render(request, 'wizard/Yandex.html', {'form': form})

def brave(request):
    form = SearchQueryForm(request.GET or None) 
    return render(request, 'wizard/Brave.html', {'form': form})

def edge(request):
    form = SearchQueryForm(request.GET or None) 
    return render(request, 'wizard/Edge.html', {'form': form})