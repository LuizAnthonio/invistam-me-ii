from urllib import request
from django.shortcuts import render, redirect,HttpResponse
from invista_me.models import Investimento
from .forms import InvestimentoForm

def pagina_inicial(request):
    fun = Investimento.objects.filter(valor__gt=200)


    fun2 = Investimento.objects.all()
    return HttpResponse(f'pronto para investir = {fun} e {fun2}',fun)

def contatos(request):
    return HttpResponse('contato')

def minha_historia(request):

    pessoa = {
        'nome':'Aoi',
        'idade': 20,
        'hobby': 'Programa da Takata'
        
            }
    return render(request,'investimentos/minha_historia.html',pessoa)


#def novo_investimento(request):
 #   return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    # print(investimento['tipo_investimento'])
    return render(request,'investimentos/investimento_registrado.html',investimento)

def investimento(request):
    total = Investimento.objects.filter(valor__gt=0).all()
    total2 = []
    da = len(total)

    for i in range(0,da):

        print(total[i].valor)
        total2.append(total[i].valor)

    print(sum(total2))

    total3 = sum(total2)


    dados = {
        'dados':Investimento.objects.all(),
        #'dados2': Investimento.objects.filter(valor__gt=200)
        'total':round(total3,2)

    }





    return render(request,'investimentos/investimento.html',dados)



def detalhe(request,id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
        }

    return render(request,'investimentos/detalhe.html',dados)


def criar(request):
    #se o metodo for tipo POST
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        #veja se é válido
        if investimento_form.is_valid():
            #salve no banco de dados
            investimento_form.save()
        #redirecione para o inicio para o name(palavra chave) da url
        return redirect('investimento')
    else:   
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html',context=formulario)

def editar(request,id_investimento):

    investimento =  Investimento.objects.get(pk=id_investimento)

    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
       formulario = InvestimentoForm(request.POST,instance=investimento)

       if formulario.is_valid():
            formulario.save()
    return redirect('investimento');
       
       
       # Create your views here.

def excluir(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':
        investimento.delete()
        return redirect('investimento')

    return render(request, 'investimentos/confirmar_exclusao.html',{'item':investimento})