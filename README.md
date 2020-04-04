==================================
Municípios Brasileiros para Django
==================================


Carregando dados de Municípios no db
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
    
    python manage.py loaddata municipios.json


Utilizando o widget de Seleção de Municípios
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

::

    from django import forms
    from municipios.widgets import SelectMunicipioWidget

    class FormEndereco(forms.Form):
        municipio = forms.IntegerField(label=u"UF - Município", widget=SelectMunicipioWidget)


View
~~~~

::

     def teste(request):
         form = FormEndereco()
         return render_to_response('endereco/teste.html', 
                {'form':form,}, context_instance = RequestContext(request))


Template
~~~~~~~~  
1. Inclua o jquery no seu template, ou adicione ao media do seu Form.
2. form.media - o widget depende de codigo js para funcionar o ajax

::

    <script type="text/javascript" src="{{ STATIC_URL }}js/jquery.min.js"></script>

    {{ form.media }}

    {{ form }}